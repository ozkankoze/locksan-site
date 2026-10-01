(function(){
  var $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};

  // Sticky header gölgesi
  var hdr=$('header.site');
  if(hdr){var sc=null,tick=false,onScroll=function(){tick=false;var s=window.pageYOffset>10;if(s!==sc){sc=s;hdr.classList.toggle('scrolled',s)}};
    requestAnimationFrame(onScroll);window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});}

  // Mobil menü
  var burger=$('.burger');
  if(burger){burger.addEventListener('click',function(){var o=document.body.classList.toggle('menu-open');burger.setAttribute('aria-label',o?'Menüyü kapat':'Menüyü aç');});}
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
})();
