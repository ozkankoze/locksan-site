"""Kullanım: python3 araclar/kontrol.py slug1 slug2 ...
Yeni yazılarda kırık iç link, bozuk JSON-LD ve listelere eklenip eklenmediğini kontrol eder."""
import re, os, sys, json, urllib.parse
D=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'site')
ok=True
for s in sys.argv[1:]:
    f=f'{D}/post/{s}.html'
    if not os.path.exists(f): print('YOK:',s); ok=False; continue
    t=open(f).read(); bad=[]
    for h in set(re.findall(r'href="(/[^"#?]*)"',t)):
        h=urllib.parse.unquote(h).rstrip('/')
        if h and not any(os.path.exists(D+h+x) for x in ('.html','','/index.html')): bad.append(h)
    for js in re.findall(r'<script type="application/ld\+json">(.*?)</script>',t,re.S):
        try: json.loads(js)
        except Exception as e: bad.append('JSON-LD: '+str(e))
    for name in ['blog.html','index.html','sitemap.xml','llms.txt']:
        if s not in open(f'{D}/{name}').read(): bad.append('listede yok: '+name)
    for img in [f'{D}/assets/blog/{s}.webp',f'{D}/assets/blog/{s}-k.webp']:
        if not os.path.exists(img): bad.append('kapak yok: '+img)
    print(s,'OK' if not bad else bad); ok=ok and not bad
sys.exit(0 if ok else 1)
