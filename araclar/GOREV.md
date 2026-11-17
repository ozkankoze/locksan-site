# Locksan Safety — günlük blog görevi

Site: https://www.locksansafety.com · Depo: ozkankoze/locksan-site (main) · Vercel kök dizini `site/` (push sonrası otomatik yayın).
Bu klasör (`araclar/`) yayınlanmaz; blog ekleme araçlarıdır.

## Kurulum
`pip install --break-system-packages pillow numpy fonttools` (eksikse)

## Yeni yazı ekleme
1. `araclar/yazilar/` içindeki son dosyayı (ör. `posts_0511.py`) örnek al; aynı yapıda `araclar/yazilar/posts_YYYYMMDD.py` yaz.
   - Her yazı: `slug, date (ISO, Z), title, seo_title (… | Locksan Safety), desc (≈150-170 karakter), faq (5 soru), body (f-string), cover_lines (3 kısa satır), letter (2-4 harf/rakam, kapak kutusu), lab (kısa etiket), step ('Uygulama Rehberi' / 'Ürün Rehberi' / 'Prosedür Rehberi')`.
   - `P` listesinde en yeni yazı İLK sırada olur (ikinci yazının saati ilkinden 10 dk geç olsun ve listede ilk yer alsın).
   - Gövde: giriş paragrafı, bir tablo (`table(...)`), adım adım `<ol>`, “Sık Yapılan Hatalar”, “Önerilen Setler” (`set_rows([...])`, yalnızca sitede bulunan LS- set kodları), iç linkler (`/post/...`, kategori sayfaları, `/teklif-sepeti`), sonda `{PIL}`.
   - Yalnızca sitede VAR OLAN sayfalara link ver (`ls site/post`, `ls site/*.html`).
2. Çalıştır: `python3 araclar/yazilar/posts_YYYYMMDD.py`  → yazı sayfaları, kapaklar, blog listesi, ana sayfa, “Son Yazılar”, sitemap ve llms.txt güncellenir.
3. Kontrol: `python3 araclar/kontrol.py <slug1> <slug2>` → hepsi OK olmalı. Kapak görselini (`site/assets/blog/<slug>.webp`) aç ve yazıların taşmadığını kontrol et.
4. `git add -A && git commit -m "Blog: <konu1> ve <konu2>" && git push origin main`

## Kurallar
- Konu tekrarı yok: `ls site/post` ve `araclar/yazilar/*.py` içindeki slug ve başlıklara bak. Konular EKED/LOTO odaklı, SEO uyumlu, Türkçe.
- Ürün kodu, fiyat, mevzuat maddesi uydurma. Emin olmadığın teknik iddiayı genel ifade et.
- `site/` altındaki tasarıma, CSS'e ve diğer sayfaların içeriğine dokunma.
