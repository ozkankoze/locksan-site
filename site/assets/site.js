(function(){
  var $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};

  // Sticky header gölgesi
  var hdr=$('header.site');
  if(hdr){var sc=null,tick=false,onScroll=function(){tick=false;var s=window.pageYOffset>10;if(s!==sc){sc=s;hdr.classList.toggle('scrolled',s)}};
    requestAnimationFrame(onScroll);window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});}

  // Mobil menü
  var burger=$('.burger');
  var setTop=function(){if(hdr)document.documentElement.style.setProperty('--mtop',Math.max(0,Math.round(hdr.getBoundingClientRect().bottom))+'px')};
  window.addEventListener('resize',setTop);
  if(burger){burger.addEventListener('click',function(){setTop();var o=document.body.classList.toggle('menu-open');burger.setAttribute('aria-label',o?'Menüyü kapat':'Menüyü aç');});}
  $$('#menu a').forEach(function(a){a.addEventListener('click',function(){document.body.classList.remove('menu-open')})});

  // Ürünlerimiz açılır menü
  var drop=$('.has-drop');
  if(drop){var dbtn=drop.querySelector('button');
    dbtn.addEventListener('click',function(e){e.stopPropagation();var o=drop.classList.toggle('open');dbtn.setAttribute('aria-expanded',o);});
    document.addEventListener('click',function(e){if(!drop.contains(e.target)){drop.classList.remove('open');dbtn.setAttribute('aria-expanded','false')}});}

  // Site içi arama
  // Arama dizini ilk kullanımda yüklenir (sayfa açılışını yavaşlatmaz)
  var pages=[],idxState=0,loadIdx=function(cb){if(idxState===2){cb&&cb();return}var q=loadIdx.q=loadIdx.q||[];cb&&q.push(cb);if(idxState)return;idxState=1;
    var sc=document.createElement('script');sc.src='/assets/search.js?v='+(document.documentElement.getAttribute('data-v')||'');sc.async=true;
    sc.onload=function(){pages=window.LOCKSAN_SEARCH||[];idxState=2;q.forEach(function(f){f()})};document.head.appendChild(sc)};
  var norm=function(s){return s.toLocaleLowerCase('tr').replace(/ı/g,'i').replace(/ğ/g,'g').replace(/ü/g,'u').replace(/ş/g,'s').replace(/ö/g,'o').replace(/ç/g,'c').replace(/[’'|]/g,'').replace(/\s+/g,' ')};
  $$('[data-search]').forEach(function(inp){
    var box=inp.parentNode.querySelector('.results');
    var render=function(){
      var q=norm(inp.value.trim());
      if(!q){box.classList.remove('show');return}
      var words=q.split(' ');
      var hits=pages.filter(function(p){var n=norm(p[0]);return words.every(function(w){return n.indexOf(w)>-1})}).slice(0,12);
      box.innerHTML=hits.length?hits.map(function(p,i){return '<a'+(i===0?' class="hl"':'')+' href="'+p[1]+'">'+p[0]+'</a>'}).join(''):'<p>Sonuç bulunamadı</p>';
      box.classList.add('show');
    };
    var go=function(){loadIdx(render)};
    inp.addEventListener('input',go);inp.addEventListener('focus',go);inp.addEventListener('pointerenter',function(){loadIdx()},{once:true});
    inp.addEventListener('keydown',function(e){if(e.key==='Enter'){var f=box.querySelector('a');if(f)location.href=f.href}if(e.key==='Escape'){box.classList.remove('show')}});
    document.addEventListener('click',function(e){if(!inp.parentNode.contains(e.target))box.classList.remove('show')});
  });

  // İletişim formu → e-posta
  $$('form[data-contact]').forEach(function(form){
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var em=form.email,msg=form.mesaj,ok=true;
      [em,msg].forEach(function(f){f.style.borderColor=''});
      if(!/^\S+@\S+\.\S+$/.test(em.value)){em.style.borderColor='#D32F2F';ok=false}
      if(!msg.value.trim()){msg.style.borderColor='#D32F2F';ok=false}
      if(!ok)return;
      var body='Ad: '+form.ad.value+'\nSoyad: '+form.soyad.value+'\nEmail: '+em.value+'\nTelefon: '+form.telefon.value+'\nSayfa: '+location.href+'\n\n'+msg.value;
      var note=form.querySelector('.form-note');if(note)note.style.display='block';
      location.href='mailto:info@locksansafety.com?subject='+encodeURIComponent('Web Sitesi İletişim Formu')+'&body='+encodeURIComponent(body);
    });
  });

  // Ürün galerisi
  $$('.gallery').forEach(function(g){
    var main=g.querySelector('.main img');
    $$('.thumbs button',g).forEach(function(b){
      b.addEventListener('click',function(){
        main.src=b.getAttribute('data-full');main.alt=b.querySelector('img').alt;
        $$('.thumbs button',g).forEach(function(x){x.classList.remove('on')});b.classList.add('on');
      });
    });
  });

  // Görünür oldukça animasyon
  var io='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}})},{threshold:.08,rootMargin:'0px 0px -30px 0px'}):null;
  $$('.rv').forEach(function(el,i){el.style.transitionDelay=(i%4)*60+'ms';io?io.observe(el):el.classList.add('in')});

  // Sayaçlar
  var cio='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(en){if(!en.isIntersecting)return;var el=en.target,t=+el.dataset.count,s=performance.now();cio.unobserve(el);
    (function tick(n){var p=Math.min((n-s)/1400,1),v=Math.round(t*(1-Math.pow(1-p,3)));el.textContent=(el.dataset.fmt==='dot'?v.toLocaleString('tr-TR'):v)+'+';if(p<1)requestAnimationFrame(tick)})(s);
  })},{threshold:.6}):null;
  if(cio)$$('[data-count]').forEach(function(el){cio.observe(el)});

  var yr=document.getElementById('yr');if(yr)yr.textContent=new Date().getFullYear();

document.querySelectorAll('[data-reffilter]').forEach(function(bar){
  var btns=bar.querySelectorAll('button'),cards=document.querySelectorAll('.refcard');
  btns.forEach(function(b){b.addEventListener('click',function(){
    btns.forEach(function(x){x.classList.toggle('on',x===b)});
    var f=b.getAttribute('data-f');
    cards.forEach(function(c){c.classList.toggle('hide',f!=='all'&&c.getAttribute('data-s')!==f)});
  })});
});

  // ===== Teklif sepeti =====
  var QK='locksan_teklif',qget=function(){try{var v=JSON.parse(localStorage.getItem(QK)||'[]');return Array.isArray(v)?v:[]}catch(e){return []}},
      qset=function(a){try{localStorage.setItem(QK,JSON.stringify(a))}catch(e){}qbadge()},
      qbadge=function(){var n=qget().reduce(function(s,x){return s+(+x.q||0)},0);$$('[data-qn]').forEach(function(el){el.textContent=n>99?'99+':n;el.hidden=!n})},
      qesc=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})},
      qtoast=function(name){var t=$('.qtoast');if(!t){t=document.createElement('div');t.className='qtoast';t.setAttribute('role','status');document.body.appendChild(t)}
        t.innerHTML='<span><b>'+qesc(name)+'</b> teklif sepetine eklendi</span><a href="/teklif-sepeti">Sepete Git</a>';t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(function(){t.classList.remove('show')},3200)};
  qbadge();window.addEventListener('storage',qbadge);
  $$('[data-qty]').forEach(function(w){var i=w.querySelector('input');$$('button',w).forEach(function(b){b.addEventListener('click',function(){i.value=Math.max(1,Math.min(9999,(parseInt(i.value,10)||1)+(+b.getAttribute('data-d'))));i.dispatchEvent(new Event('change'))})})});
  $$('[data-add]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();
    var box=b.closest('.qadd'),qi=box&&box.querySelector('[data-qty] input'),q=Math.max(1,parseInt(qi&&qi.value,10)||1),
        it={code:b.getAttribute('data-code'),name:b.getAttribute('data-name'),img:b.getAttribute('data-img'),url:b.getAttribute('data-url'),q:q},a=qget(),f=null;
    a.forEach(function(x){if(x.url===it.url)f=x});if(f)f.q=Math.min(9999,(+f.q||0)+q);else a.push(it);qset(a);
    var c=$('.qcart');if(c){c.classList.remove('bump');void c.offsetWidth;c.classList.add('bump')}
    var old=b.innerHTML;b.classList.add('ok');b.innerHTML=b.classList.contains('padd')?'✓ Eklendi':'✓ Sepete Eklendi';setTimeout(function(){b.classList.remove('ok');b.innerHTML=old},1600);
    qtoast(((it.code||'')+' '+(it.name||'')).trim());
  })});
  var qp=$('[data-qpage]');
  if(qp){
    var list=$('.qlist',qp),form=$('.qform',qp),sum=$('.qsum',qp);
    var draw=function(){var a=qget();
      if(!a.length){list.innerHTML='<div class="qempty"><svg><use href="#i-cart"/></svg><h2>Teklif sepetiniz boş</h2><p>Ürün sayfalarındaki <b>Teklif Sepetine Ekle</b> veya kartlardaki <b>+ Teklif</b> düğmesiyle ürün ekleyebilirsiniz.</p><a class="btn btn-red" href="/etiketleme-kilitleme-urunleri">Ürünlere Göz At</a></div>';sum.hidden=true;form.setAttribute('data-empty','');return}
      form.removeAttribute('data-empty');sum.hidden=false;
      list.innerHTML=a.map(function(x,i){return '<div class="qitem" data-i="'+i+'"><a class="im" href="'+qesc(x.url)+'">'+(x.img?'<img src="'+qesc(x.img)+'" alt="'+qesc(x.name)+'" loading="lazy">':'<b>'+qesc(x.code)+'</b>')+'</a>'+
        '<div>'+(x.code?'<span class="code">'+qesc(x.code)+'</span>':'')+'<a class="nm" href="'+qesc(x.url)+'">'+qesc(x.name)+'</a></div>'+
        '<div class="qty sm"><button type="button" data-d="-1" aria-label="Azalt">−</button><input type="number" min="1" max="9999" value="'+(+x.q||1)+'" aria-label="Adet"><button type="button" data-d="1" aria-label="Arttır">+</button></div>'+
        '<button type="button" class="rm" aria-label="Kaldır" title="Kaldır">×</button></div>'}).join('');
      var n=a.reduce(function(s,x){return s+(+x.q||0)},0);$('.qsum span',qp).innerHTML='<b>'+a.length+'</b> ürün · toplam <b>'+n+'</b> adet';
    };
    list.addEventListener('click',function(e){var row=e.target.closest('.qitem');if(!row)return;var i=+row.getAttribute('data-i'),a=qget();
      if(e.target.closest('.rm')){a.splice(i,1);qset(a);draw();return}
      var d=e.target.closest('[data-d]');if(d){a[i].q=Math.max(1,Math.min(9999,(+a[i].q||1)+(+d.getAttribute('data-d'))));qset(a);draw()}});
    list.addEventListener('change',function(e){if(e.target.tagName!=='INPUT')return;var row=e.target.closest('.qitem'),a=qget(),i=+row.getAttribute('data-i');a[i].q=Math.max(1,Math.min(9999,parseInt(e.target.value,10)||1));qset(a);draw()});
    $('.qsum button',qp).addEventListener('click',function(){qset([]);draw()});
    var F=function(n){return form.querySelector('[name="'+n+'"]')};
    try{var sv=JSON.parse(localStorage.getItem('locksan_teklif_bilgi')||'{}');['ad','firma','tel','eposta'].forEach(function(k){if(sv[k])F(k).value=sv[k]})}catch(e){}
    var msg=function(){var a=qget(),L=['Merhaba, aşağıdaki ürünler için fiyat teklifi rica ediyorum.',''];
      a.forEach(function(x,i){L.push((i+1)+') '+(x.code?x.code+' – ':'')+x.name+' × '+x.q+' adet')});
      L.push('');[['Ad Soyad','ad'],['Firma','firma'],['Telefon','tel'],['E-posta','eposta']].forEach(function(p){var v=F(p[1]).value.trim();if(v)L.push(p[0]+': '+v)});
      var nt=F('not').value.trim();if(nt){L.push('');L.push('Not: '+nt)}return L.join('\n')};
    var check=function(){var ok=true;['ad','tel'].forEach(function(k){var f=F(k),bad=!f.value.trim();f.classList.toggle('err',bad);if(bad)ok=false});
      var em=F('eposta');if(em.value.trim()&&!/^\S+@\S+\.\S+$/.test(em.value.trim())){em.classList.add('err');ok=false}else em.classList.remove('err');
      if(!ok){var f=form.querySelector('.err');f&&f.focus()}
      try{localStorage.setItem('locksan_teklif_bilgi',JSON.stringify({ad:F('ad').value,firma:F('firma').value,tel:F('tel').value,eposta:F('eposta').value}))}catch(e){}
      return ok&&qget().length};
    $('[data-send="wa"]',qp).addEventListener('click',function(){if(check())window.open('https://wa.me/905078914728?text='+encodeURIComponent(msg()),'_blank','noopener')});
    $('[data-send="mail"]',qp).addEventListener('click',function(){if(check())location.href='mailto:info@locksansafety.com?subject='+encodeURIComponent('Teklif Talebi – '+(F('firma').value.trim()||F('ad').value.trim()))+'&body='+encodeURIComponent(msg())});
    draw();window.addEventListener('storage',draw);
  }
})();
