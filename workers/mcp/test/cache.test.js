import test from 'node:test';
import assert from 'node:assert/strict';

test('failures retry, paths do not collide, metadata and bodies expire', async () => {
  const originalFetch = globalThis.fetch, originalNow = Date.now;
  let now = 1000, calls = 0, fail = true, indexFail = false;
  Date.now = () => now;
  globalThis.fetch = async url => {
    if (String(url).endsWith('articles.json')) return indexFail ? new Response('', {status:503}) : Response.json([
      {path:'People/same.md', category:'People', title:'People'},
      {path:'Politics/same.md', category:'Politics', title:'Politics'},
    ]);
    calls++;
    return fail ? new Response('', {status:503}) : new Response(`body ${url} version ${now}`);
  };
  try {
    const {default:worker} = await import('../src/index.js?cache-test');
    const read = async slug => (await (await worker.fetch(new Request('https://test/', {method:'POST',body:JSON.stringify({jsonrpc:'2.0',id:1,method:'tools/call',params:{name:'taiwanmd_read',arguments:{slug}}})}))).json()).result;
    assert.equal((await read('People/same.md')).isError, true);
    fail = false;
    assert.match((await read('People/same.md')).content[0].text, /version 1000/);
    assert.equal(calls, 2);
    await read('People/same.md'); assert.equal(calls, 2);
    assert.match((await read('Politics/same.md')).content[0].text, /raw\/politics/);
    assert.equal((await read('same')).isError, true);
    now += 1800001;
    assert.match((await read('People/same.md')).content[0].text, /version 1801001/);
    now += 1800001; indexFail = true;
    assert.equal((await read('People/same.md')).isError, true);
    indexFail = false;
    assert.equal((await read('People/same.md')).isError, undefined);
  } finally {globalThis.fetch = originalFetch; Date.now = originalNow;}
});
