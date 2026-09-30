# Locksan Safety – Yeni Site

Bu klasörde Wix'teki sitenin modernleştirilmiş, statik (HTML/CSS/JS) hali var.
**`site/` klasörü yayına alınacak klasördür.** Toplam 229 sayfa + 404 sayfası.

## Önizleme (Mac)
`Önizleme.command` dosyasına çift tıklayın → tarayıcıda http://localhost:8765 açılır.
(İlk seferde macOS izin sorarsa: dosyaya sağ tık → Aç.)
`site/index.html` dosyasını doğrudan çift tıklayarak açmayın; linkler kök dizine göre (/sayfa) yazıldığı için bir sunucu gerekir.

## URL yapısı (SEO)
- Wix'teki **tüm adresler birebir korundu** (ör. `/emniyet-asma-kilitler`, `/ls-g01/red`, `/post/...`, `/blog/categories/...`).
- Her sayfa `sayfa-adi.html` olarak kaydedildi; sunucu `/sayfa-adi` isteğini bu dosyaya yönlendirir (sonunda .html görünmez).
- Başlık (title), açıklama (description) ve canonical etiketleri Wix'teki değerlerle aynıdır.
- `sitemap.xml` ve `robots.txt` hazır. Yayına aldıktan sonra Google Search Console'da sitemap'i yeniden gönderin.

## Yayına alma
Hangi hosting'i kullanırsanız kullanın `site/` klasörünün **içeriğini** yükleyin:
- **cPanel / Apache hosting:** `.htaccess` hazır (temiz URL, www ve https yönlendirmesi, 404). Gizli dosyaları göstermeyi açıp `.htaccess`'in yüklendiğinden emin olun.
- **Netlify:** Klasörü sürükleyip bırakın (`_redirects` hazır, temiz URL'ler otomatik).
- **Vercel:** `vercel.json` hazır (`cleanUrls`).
- **Cloudflare Pages:** Ek ayar gerekmez.

## Taşımadan önce yapılacaklar
1. **Görseller** şu an Wix'in görsel sunucusundan (static.wixstatic.com) geliyor. Wix aboneliğini kapatmadan önce görselleri kendi sunucunuza almamız gerekir – isterseniz bu adımı da yapabilirim.
2. **Katalog PDF** eski adresinden (Wix dosya sunucusu) yönlendiriliyor. PDF'i `site/` içine koyup linki güncelleyebilirim.
3. **İletişim formu** şu an ziyaretçinin e-posta uygulamasını açar. Mesajların doğrudan gelmesi için Formspree/Netlify Forms gibi bir servise bağlanabilir.
4. Alan adının DNS kayıtlarını yeni hosting'e yönlendirin (Wix'ten çıkarken).

## İçerik notları
- 2 sayfanın başlığı Wix'te başka ürüne aitti, düzeltildi: `/ls-f22-ayarlanabilir-kelebek-vana-kilitleme` (LS-F21 yazıyordu), `/ls-x03/guvenlik-kilitleme-kutusu` (LS-X04 yazıyordu).
- Başlığı sadece "Locksan Safety" olan ürün sayfalarına ürün adı + kategori içeren başlık ve açıklama eklendi.
- Tüm ürün sayfalarına Google için ürün (Product) ve sayfa yolu (Breadcrumb) yapısal verisi eklendi.
- `/blank-1` (Wix'te zaten 404 veren boş sayfa) üretilmedi.
