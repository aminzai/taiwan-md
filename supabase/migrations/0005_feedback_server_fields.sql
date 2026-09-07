-- Server-owned timestamps and triage fields; serialize each user's hourly quota.
-- Additive migration: keep previous migrations as deployed history.
begin;
create or replace function public.feedback_rate_limit()
returns trigger language plpgsql volatile security definer
set search_path = pg_catalog, public as $$
declare
  recent_count integer;
begin
  -- Always count server time, even when the caller supplies a backdated value.
  new.created_at := clock_timestamp();
  if current_setting('role', true) = 'authenticated' then
    new.status := 'new';
    new.issue_url := null;
    new.issue_number := null;
    new.triaged_at := null;
    new.triage_note := null;
  end if;
  -- Transaction-scoped lock prevents concurrent inserts from sharing quota.
  perform pg_advisory_xact_lock(hashtextextended(new.uid::text, 0));
  select count(*) into recent_count from public.feedback
    where uid = new.uid and created_at > clock_timestamp() - interval '1 hour';
  if recent_count >= 20 then
    raise exception 'feedback rate limit exceeded (20/hour)';
  end if;
  return new;
end;
$$;
revoke all on function public.feedback_rate_limit() from public;
-- Clients submit content only. Defaults and the trigger own system fields.
revoke insert on public.feedback from anon, authenticated;
grant insert (uid, display_name, article_slug, article_title, category, lang,
              source_url, type, body, correct_info, quote, page_kind)
  on public.feedback to authenticated;
create index if not exists feedback_uid_created_at_idx on public.feedback (uid, created_at);
commit;
