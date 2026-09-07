"""Disposable PostgreSQL integration test. Requires TWMD_TEST_DATABASE_URL.
Never target production: creates a uniquely named database and drops it on exit.
Run: TWMD_TEST_DATABASE_URL=postgresql://.../postgres python tests/feedback/database.test.py
"""
import os
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import psycopg
from psycopg import sql

url = os.environ['TWMD_TEST_DATABASE_URL']
name = 'twmd_feedback_test_' + uuid.uuid4().hex[:12]
root = psycopg.connect(url, autocommit=True)
root.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier(name)))
params = psycopg.conninfo.conninfo_to_dict(url)
params['dbname'] = name
try:
    with psycopg.connect(**params, autocommit=True) as db:
        for role in ['anon','authenticated','service_role']:
            if not root.execute('SELECT 1 FROM pg_roles WHERE rolname=%s', (role,)).fetchone():
                root.execute(sql.SQL('CREATE ROLE {} NOLOGIN').format(sql.Identifier(role)))
        root.execute("ALTER ROLE service_role BYPASSRLS")
        db.execute("CREATE SCHEMA auth; CREATE TABLE auth.users(id uuid PRIMARY KEY)")
        db.execute("CREATE FUNCTION auth.uid() RETURNS uuid LANGUAGE sql STABLE AS $$ SELECT nullif(current_setting('request.jwt.claim.sub',true),'')::uuid $$")
        db.execute('GRANT USAGE ON SCHEMA auth,public TO authenticated,service_role; GRANT EXECUTE ON FUNCTION auth.uid() TO authenticated')
        for migration in sorted((Path(__file__).resolve().parents[2]/'supabase/migrations').glob('*.sql')):
            db.execute(migration.read_text())
            # Emulate Supabase default table grants before the hardening migration.
            if migration.name.startswith('0001'):
                db.execute('GRANT ALL ON public.feedback TO authenticated,service_role')
        user = str(uuid.uuid4())
        db.execute('INSERT INTO auth.users VALUES (%s)', (user,))
        def insert(extra='', suffix=''):
            try:
                with psycopg.connect(**params, autocommit=True) as conn:
                    conn.execute('SET ROLE authenticated')
                    conn.execute("SELECT set_config('request.jwt.claim.sub',%s,false)", (user,))
                    conn.execute(f"INSERT INTO public.feedback(uid,display_name,type,body{extra}) VALUES (%s,'reader','bug','test report'{suffix})", (user,))
                return True
            except psycopg.Error:
                return False
        assert not insert(',created_at', ", '2000-01-01'"), 'client timestamp must be rejected'
        assert not insert(',issue_number', ', 99'), 'system field must be rejected'
        assert not insert(',status', ", 'filed'"), 'client status must be rejected'
        with ThreadPoolExecutor(max_workers=25) as pool:
            results = list(pool.map(lambda _:insert(), range(25)))
        assert sum(results) == 20, results
        assert not insert(), '21st request must fail'
        count, fresh = db.execute("SELECT count(*), bool_and(created_at > now()-interval '1 minute') FROM public.feedback").fetchone()
        assert count == 20 and fresh
        # Supabase service-role triage still works after column restrictions.
        db.execute("SET ROLE service_role")
        db.execute("UPDATE public.feedback SET status='filed',issue_number=42")
        assert db.execute("SELECT count(*) FROM public.feedback WHERE issue_number=42").fetchone()[0] == 20
        db.execute('RESET ROLE')
        print('PASS: server timestamp, protected fields, 25 concurrent requests => 20 inserts, request 21 rejected, triage update')
finally:
    root.execute(sql.SQL('DROP DATABASE {} WITH (FORCE)').format(sql.Identifier(name)))
    root.close()
