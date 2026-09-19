import re,html,sys
s=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
s=re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>','',s,flags=re.S)
t=re.sub(r'<br\s*/?>','\n',s); t=re.sub(r'</p>','\n',t)
t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
t=re.sub(r'[ \t　]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
open(sys.argv[1].rsplit('.',1)[0]+'.txt','w').write(t)
print(len(t))
