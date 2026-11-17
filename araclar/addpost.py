import re, json, glob, os, html, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import cover
D=os.path.join(os.path.dirname(HERE),'site'); SITE='https://www.locksansafety.com'
AY=['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
def tr_date(iso): y,m,d=iso[:10].split('-'); return f'{int(d)} {AY[int(m)-1]} {y}'
PIL='<a href="/etiketleme-kilitleme-urunleri">etiketleme kilitleme ürünleri</a>'
def table(head,rows):
    h=''.join(f'<th>{x}</th>' for x in head)
    b=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<div class="tbl"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'
_ROWS={}
for f in glob.glob(D+'/post/*.html'):
    for m in re.finditer(r'<tr><td><a href="([^"]+)" title="(LS-[^"]+)">[^<]*</a></td><td>([^<]*)</td><td>([^<]*)</td></tr>',open(f).read()):
        _ROWS[m.group(2)]=(m.group(1),m.group(3),m.group(4))
def set_rows(codes): return [[f'<a href="{_ROWS[c][0]}">{c}</a>',_ROWS[c][1],_ROWS[c][2]] for c in codes]
def faq_html(F): return '<h2>Sıkça Sorulan Sorular</h2>'+''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in F)
def add_titles(s):
    def fix(m):
        tag,txt=m.group(1),m.group(2)
        if 'title=' in tag: return m.group(0)
        plain=html.unescape(re.sub('<[^>]+>','',txt)).replace('"','&quot;')
        return tag[:-1]+f' title="{plain}">'+txt+'</a>'
    return re.sub(r'(<a [^>]*>)(.*?)</a>',fix,s)
def trunc(s,n):
    if len(s)<=n: return s
    return s[:n].rsplit(' ',1)[0].rstrip(',;:')+'…'
def card(p):
    ttl=f"{tr_date(p['date'])} {p['title']} {p['desc']}"[:120]
    return (f'<a class="pcard wide bcard rv" href="/post/{p["slug"]}" title="{html.escape(ttl,quote=True)}"><div class="ph"><img loading="lazy" src="/assets/blog/{p["slug"]}.webp" alt="{html.escape(p["title"],quote=True)}" width="1600" height="900" decoding="async"></div>'
            f'<div class="bd"><span class="date">{tr_date(p["date"])}</span><h2>{p["title"]}</h2><p class="desc">{trunc(p["desc"],140)}</p><span class="more">Yazıyı Oku <svg><use href="#i-arrow"/></svg></span></div></a>')
TPL_SLUG='kompresor-bakiminda-loto'
def build_page(p):
    t=open(f'{D}/post/{TPL_SLUG}.html').read()
    old=re.search(r'<h1>(.*?)</h1>',t).group(1)
    oseo=re.search(r'<title>(.*?)</title>',t).group(1)
    odesc=re.search(r'<meta name="description" content="(.*?)">',t).group(1)
    t=t.replace(f'<title>{oseo}</title>',f'<title>{p["seo_title"]}</title>').replace(f'content="{oseo}"',f'content="{p["seo_title"]}"')
    t=t.replace(odesc,html.escape(p['desc'],quote=True))
    t=t.replace(json.dumps(html.unescape(odesc),ensure_ascii=False)[1:-1],json.dumps(p['desc'],ensure_ascii=False)[1:-1])
    t=t.replace(old,p['title']).replace(json.dumps(old,ensure_ascii=False)[1:-1],json.dumps(p['title'],ensure_ascii=False)[1:-1])
    t=t.replace(TPL_SLUG,p['slug'])
    t=re.sub(r'"datePublished": "[^"]+", "dateModified": "[^"]+"',f'"datePublished": "{p["date"]}", "dateModified": "{p["date"]}"',t)
    t=re.sub(r'(<div class="post-meta"><span>Locksan Safety</span><span>)[^<]+',r'\g<1>'+tr_date(p['date']),t)
    faq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p['faq']]}
    t=re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>','<script type="application/ld+json">'+json.dumps(faq,ensure_ascii=False).replace('\\','\\\\')+'</script>',t,flags=re.S)
    body=add_titles(p['body'].strip()+'\n'+faq_html(p['faq']))
    t=re.sub(r'(<article class="post-body prose">).*?(</article>)',lambda m:m.group(1)+body+m.group(2),t,flags=re.S)
    return t
def update_lists(new_posts):
    b=open(f'{D}/blog.html').read()
    first=b.find('<a class="pcard wide bcard rv"')
    b=b[:first]+''.join(card(p) for p in new_posts)+b[first:]
    open(f'{D}/blog.html','w').write(b)
    cards=re.findall(r'<a class="pcard wide bcard rv" href="/post/([^"]+)".*?</a>',b)
    full={m.group(1):m.group(0) for m in re.finditer(r'<a class="pcard wide bcard rv" href="/post/([^"]+)".*?</a>',b)}
    order=[m.group(1) for m in re.finditer(r'<a class="pcard wide bcard rv" href="/post/([^"]+)"',b)]
    for f in glob.glob(f'{D}/post/*.html'):
        slug=os.path.basename(f)[:-5]; t=open(f).read()
        pat=re.compile(r'(<h2>Son Yazılar</h2>.*?<div class="pgrid"[^>]*>)(.*?)(</div></div></section>)',re.S)
        if not pat.search(t): continue
        sel=[full[s] for s in order if s!=slug][:3]
        t=pat.sub(lambda m:m.group(1)+''.join(sel)+m.group(3),t,count=1); open(f,'w').write(t)
    # index
    t=open(f'{D}/index.html').read()
    def info(s):
        c=full[s]; ti=re.search(r'<h2>(.*?)</h2>',c).group(1); dt=re.search(r'<span class="date">(.*?)</span>',c).group(1)
        de=re.search(r'title="(.*?)"',c).group(1); ds=re.search(r'<p class="desc">(.*?)</p>',c).group(1)
        return ti,dt,de,ds
    top=order[:4]; ti,dt,de,ds=info(top[0])
    big=(f'<a class="lp rv" href="/post/{top[0]}" title="{de}"><div class="ph"><img loading="lazy" src="/assets/blog/{top[0]}.webp" alt="{html.escape(html.unescape(ti),quote=True)}" width="900" height="506" decoding="async"></div><div class="bd"><span class="date">{dt}</span><h3>{ti}</h3><p>{ds}</p><span class="more">Yazıyı Oku <svg><use href="#i-arrow"/></svg></span></div></a>')
    side=''
    for s in top[1:]:
        ti,dt,de,ds=info(s); short=trunc(html.unescape(ds).rstrip('…'),90)
        side+=(f'<a class="lp rv" href="/post/{s}" title="{de}"><div class="ph"><img loading="lazy" src="/assets/blog/{s}-k.webp" alt="{html.escape(html.unescape(ti),quote=True)}" width="300" height="300" decoding="async"></div><div class="bd"><span class="date">{dt}</span><h3>{ti}</h3><p>{short}</p></div></a>')
    t=re.sub(r'<div class="latest">.*?</div></div>\n',lambda m:'<div class="latest">'+big+'<div class="side">'+side+'</div></div>\n',t,count=1,flags=re.S)
    open(f'{D}/index.html','w').write(t)
    # sitemap + llms
    sm=open(f'{D}/sitemap.xml').read()
    add=''.join(f'  <url><loc>{SITE}/post/{p["slug"]}</loc><lastmod>{p["date"][:10]}</lastmod></url>\n' for p in new_posts)
    sm=sm.replace('</urlset>',add+'</urlset>'); open(f'{D}/sitemap.xml','w').write(sm)
    ll=open(f'{D}/llms.txt').read(); anchor='- [Saha Araştırması]('+SITE+'/saha-arastirmasi)\n'
    ll=ll.replace(anchor,anchor+''.join(f'- [{p["title"]}]({SITE}/post/{p["slug"]})\n' for p in new_posts))
    open(f'{D}/llms.txt','w').write(ll)
def publish(posts):
    for p in posts:
        open(f'{D}/post/{p["slug"]}.html','w').write(build_page(p))
        cover.make(f'{D}/assets/blog/{p["slug"]}.webp',p['cover_lines'],p['letter'],p['lab'],p['step'])
    update_lists(posts)
