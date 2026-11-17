import os
HERE=os.path.dirname(os.path.abspath(__file__))
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
FL=os.path.join(HERE,'rhd-latin.ttf'); FX=os.path.join(HERE,'rhd-latin-ext.ttf')
CM=TTFont(FL).getBestCmap()
_c={}
def font(path,size,w):
    k=(path,size,w)
    if k not in _c:
        f=ImageFont.truetype(path,size,layout_engine=ImageFont.Layout.BASIC); f.set_variation_by_name({400:'Regular',450:'Regular',500:'Medium',600:'SemiBold',700:'Bold',800:'ExtraBold',900:'Black'}[w]); _c[k]=f
    return _c[k]
def tw(t,size,w): return sum(font(FL if ord(ch) in CM else FX,size,w).getlength(ch) for ch in t)
def draw(d,xy,t,size,w,fill,anchor_center=False):
    x,y=xy
    if anchor_center: x-=tw(t,size,w)/2
    for ch in t:
        f=font(FL if ord(ch) in CM else FX,size,w)
        d.text((x,y),ch,font=f,fill=fill,anchor='ls'); x+=f.getlength(ch)
def erase(a,x0,x1,y0,y1):
    L=a[y0:y1,x0-6:x0-2].mean(1); R=a[y0:y1,x1+2:x1+6].mean(1)
    t=np.linspace(0,1,x1-x0)[None,:,None]
    a[y0:y1,x0:x1]=(L[:,None]*(1-t)+R[:,None]*t)
def tr_upper(s): return s.replace('i','İ').replace('ı','I').upper()
def make(out, title_lines, letter, lab, step, base=os.path.join(HERE,'bg.png')):
    im=Image.open(base).convert('RGB'); d=ImageDraw.Draw(im)
    y=274
    for ln in title_lines: draw(d,(90,y),ln,90,900,(255,255,255)); y+=104
    s=200
    while tw(letter,s,900)>370: s-=6
    draw(d,(1250,390+s*0.36),letter,s,900,(255,255,255),True)
    draw(d,(1250,690),tr_upper(lab),46,900,(255,255,255),True)
    draw(d,(1250,738),tr_upper(step),30,450,(240,150,150),True)
    im.save(out,'WEBP',quality=88)
    im.crop((700,0,1600,900)).resize((600,600),Image.LANCZOS).save(out.replace('.webp','-k.webp'),'WEBP',quality=88)
