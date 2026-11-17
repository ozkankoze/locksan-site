import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from addpost import *

F1=[
 ('Trafo ve OG hücre bakımında LOTO nasıl uygulanır?','Bakım yapılacak bölüm, kesici ve ayırıcılarla tüm beslemelerden ayrılır; ayırıcılar açık konumda kilitlenir, gerilimin olmadığı uygun ölçüm cihazıyla doğrulanır, topraklama yapılır ve uyarı etiketleri asılır. Bu işler yalnızca yetkilendirilmiş elektrik personeli tarafından yapılmalıdır.'),
 ('Elektrikte “5 güvenlik kuralı” nedir?','Gerilim altında olmayan tesislerde çalışmanın temel kurallarıdır: 1) Devreyi aç (ayır), 2) Tekrar kapanmaya karşı emniyete al (kilitle), 3) Gerilim olmadığını kontrol et, 4) Topraklama ve kısa devre yap, 5) Yakındaki gerilimli bölümleri yalıt veya perdele. LOTO, bu kuralların ikinci adımının uygulamasıdır.'),
 ('Kesiciyi açmak yeterli mi?','Hayır. Kesici yük akımını keser ama görünür bir ayırma sağlamayabilir ve uzaktan kumandayla tekrar kapanabilir. İzolasyon için ayırıcı açılıp kilitlenmeli, kesicinin kumanda enerjisi de kesilmelidir.'),
 ('Trafo alçak gerilim tarafından beslenebilir mi?','Evet. Jeneratör, UPS veya başka bir trafo üzerinden alçak gerilim tarafından geri besleme olabilir. Bu nedenle trafonun AG çıkış şalteri de açılıp kilitlenmelidir.'),
 ('Hangi LOTO ürünleri gerekir?','Ayırıcı kolları ve kumanda anahtarları için emniyet asma kilitleri ve çoklayıcılar, AG panolarda açık tip (ACB) ve kompakt şalter kilitleri, grup kilitleme kutusu ve uyarı etiketleri temel ekipmanlardır.'),
]
B1=f'''
<p>Fabrikaların, AVM’lerin ve hastanelerin enerji girişindeki <b>trafo merkezleri ve orta gerilim (OG) hücreleri</b>, tesisin en yüksek enerji seviyesine sahip noktalarıdır. Burada yapılacak bir hata ölümcül sonuçlar doğurur ve ikinci bir şans tanımaz. Bu yazıda trafo ve OG hücre bakımında LOTO uygulamasını ve bilinmesi gereken temel kuralları özetliyoruz.</p>
<p><b>Önemli:</b> OG tesislerde manevra ve bakım işleri yalnızca yetkilendirilmiş elektrik personeli tarafından, ilgili mevzuata ve tesisin işletme talimatlarına uygun olarak yapılmalıdır. Bu yazı genel bilgilendirme amaçlıdır.</p>

<h2>Elektrikte 5 Güvenlik Kuralı ve LOTO</h2>
{table(['Kural','Açıklama','LOTO ile ilişkisi'],[
 ['1. Ayır','Bölümü tüm beslemelerden kesici ve ayırıcılarla ayır','İzolasyon noktalarının belirlenmesi'],
 ['2. Kilitle','Tekrar kapanmaya karşı emniyete al','Kişisel kilit + uyarı etiketi'],
 ['3. Kontrol et','Gerilim olmadığını uygun cihazla doğrula','LOTO doğrulama (dene) adımı'],
 ['4. Toprakla','Topraklama ve kısa devre yap','Topraklama ayırıcısı / portatif topraklama'],
 ['5. Perdele','Yakındaki gerilimli bölümleri yalıt','Bariyer ve uyarı levhaları'],
])}

<h2>Trafo Merkezinde Enerji Kaynakları</h2>
<ul>
<li><b>OG besleme:</b> Şebeke girişi, ring hücreleri, diğer trafolar.</li>
<li><b>AG tarafından geri besleme:</b> Jeneratör, UPS, paralel trafo veya güneş enerjisi sistemi (bkz. <a href="/post/jenerator-ve-ups-bakiminda-loto">jeneratör ve UPS bakımında LOTO</a>, <a href="/post/gunes-enerjisi-santrallerinde-ges-loto">GES’te LOTO</a>).</li>
<li><b>Depolanmış enerji:</b> Kompanzasyon kondansatörleri, kablo kapasitesi, kurulu kesici yayları.</li>
<li><b>Kumanda enerjisi:</b> Kesicilerin uzaktan açma-kapama devreleri.</li>
</ul>

<h2>Adım Adım Trafo / OG Hücre LOTO</h2>
<ol>
<li><b>Planlama:</b> Tek hat şeması üzerinden çalışılacak bölümü besleyebilecek tüm kaynaklar (OG ve AG) listelenir; manevra sırası yazılı olarak hazırlanır.</li>
<li><b>AG tarafını ayırma:</b> Trafonun AG çıkış şalteri açılır ve kilitlenir. Büyük güçlerde bu genellikle bir <a href="/post/acik-tip-devre-kesici-acb-kilitleme">açık tip devre kesicidir (ACB)</a>.</li>
<li><b>OG tarafını ayırma:</b> OG kesici açılır, ardından ayırıcı açılır. Ayırıcı kolu veya kumanda anahtarı açık konumda <a href="/emniyet-asma-kilitler">emniyet asma kilidiyle</a> kilitlenir. Kesicinin kumanda enerjisi kesilir.</li>
<li><b>Kilit ve etiket:</b> Birden fazla çalışan varsa <a href="/coklandiricilar">çoklayıcı</a> veya <a href="/post/loto-kilit-kutusu-nasil-kullanilir">grup kilitleme kutusu</a> kullanılır; tüm izolasyon noktalarına <a href="/eked-uyari-etiketleri">uyarı etiketi</a> asılır.</li>
<li><b>Gerilim kontrolü:</b> Gerilim yokluğu, ilgili gerilim seviyesine uygun gerilim dedektörüyle her fazda kontrol edilir. Bkz. <a href="/post/dene-eked-test-adimi">Dene: test adımı</a>.</li>
<li><b>Topraklama:</b> Topraklama ayırıcısı kapatılır veya portatif topraklama takılır; kompanzasyon kondansatörleri deşarj edilir.</li>
<li><b>Perdeleme:</b> Yakındaki gerilimli hücreler bariyer ve uyarı levhalarıyla ayrılır.</li>
<li><b>Devreye alma:</b> İş bitince topraklamalar kaldırılır, herkes kendi kilidini çıkarır ve manevra ters sırayla yapılır.</li>
</ol>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Kesiciyi açıp ayırıcıyı açmamak veya kilitlememek</li>
<li>AG tarafından gelebilecek geri beslemeyi unutmak</li>
<li>Gerilim kontrolünü yapmadan topraklamaya geçmek</li>
<li>Kompanzasyon kondansatörlerinin deşarjını beklememek</li>
<li>Tek kilitle tüm ekibin çalışması</li>
</ul>

<h2>Önerilen Ürünler ve Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-8812S','LS-EK-S1100VV','LS-X02C']))}
<p>Şalter tiplerine göre kilit seçimi için <a href="/post/salter-kilidi-cesitleri">şalter kilidi çeşitleri</a>, yük ayırıcılar için <a href="/post/yuk-ayirici-kilitleme">yük ayırıcı kilitleme</a> yazılarımıza bakabilirsiniz. Ekibinize özel eğitim için <a href="/egitim-ve-danismanlik">eğitim ve danışmanlık</a> sayfamızı ziyaret edin. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

F2=[
 ('Chiller ve klima santrali bakımında neden LOTO gerekir?','Bu ekipmanlar bina otomasyon sistemiyle (BMS) uzaktan veya zamanlayıcıyla otomatik çalışabilir. Ayrıca soğutucu akışkan basıncı, fanlar, kayışlar ve soğuk/sıcak su hatları gibi birden fazla enerji kaynağı bulunur. Bakım sırasında beklenmedik çalışmayı önlemek için enerji kaynakları izole edilip kilitlenmelidir.'),
 ('BMS’ten kapatmak yeterli mi?','Hayır. Bina otomasyonundan veya kumanda panelinden verilen stop komutu izolasyon değildir; program, alarm veya başka bir kullanıcı ekipmanı yeniden çalıştırabilir. Ekipmanın yerel ana şalteri veya güç beslemesi kapatılıp kilitlenmelidir.'),
 ('Fan enerjisi kesilse de dönebilir mi?','Evet. Hava akımı veya rüzgâr nedeniyle fanlar enerjisizken de dönebilir (serbest dönme). Fan veya kayış üzerinde çalışmadan önce fanın durduğu kontrol edilmeli ve gerekiyorsa mekanik olarak sabitlenmelidir.'),
 ('Soğuk su hatları nasıl izole edilir?','Bakım yapılacak ekipmanın giriş ve çıkış vanaları kapatılıp vana kilitleme ekipmanlarıyla kilitlenir, hattaki basınç tahliye edilir. HVAC tesisatında sık kullanılan kelebek ve küresel vanalar için uygun vana kilitleri seçilmelidir.'),
 ('Soğutucu akışkan devresinde nelere dikkat edilmeli?','Soğutma devresi yüksek basınç içerir. Devreye müdahale, ilgili yetkinliğe sahip personel tarafından, üretici talimatına uygun şekilde ve akışkan geri kazanımı yapılarak gerçekleştirilmelidir.'),
]
B2=f'''
<p>Hastane, AVM, otel, veri merkezi ve fabrikalarda <b>chiller, klima santrali (AHU), soğutma kulesi ve fan coil</b> gibi HVAC ekipmanları sürekli bakım gerektirir. Bu ekipmanların ortak özelliği, çoğunun <b>bina otomasyon sistemiyle (BMS) uzaktan veya otomatik olarak</b> çalışmasıdır. Teknisyen ekipmanın başındayken başka bir yerden verilen tek bir komut ciddi kazalara yol açabilir.</p>

<h2>HVAC Ekipmanlarında Enerji Kaynakları</h2>
{table(['Enerji','Nerede?','Risk','Kontrol'],[
 ['Elektrik','Kompresör, fan, pompa motorları, panolar','Otomatik veya uzaktan çalışma','<a href="/salter-kilitleme-ekipmanlari">Şalter kilidi</a> + kişisel kilit'],
 ['Mekanik','Fan, kayış-kasnak, pompa milleri','Kapılma, serbest dönen fan','Enerji kesme + fanı sabitleme'],
 ['Hidrolik / su','Soğuk ve sıcak su hatları','Basınçlı su, haşlanma','<a href="/vana-kilitleme-ekipmanlari">Vana kilidi</a> + basınç tahliyesi'],
 ['Soğutucu akışkan','Kompresör, kondenser, evaporatör','Yüksek basınç, donma yanığı','Yetkin personel, üretici talimatı'],
 ['Isıl','Sıcak su ve buhar bataryaları','Yanık','Soğuma bekleme'],
])}

<h2>Adım Adım HVAC LOTO</h2>
<ol>
<li><b>Bilgilendirme:</b> Tesis yönetimi ve BMS operatörü bilgilendirilir; ekipman otomasyonda “bakımda” olarak işaretlenir.</li>
<li><b>Durdurma:</b> Ekipman normal şekilde durdurulur.</li>
<li><b>Elektrik izolasyonu:</b> Ekipmanın yerel ana şalteri veya panodaki besleme şalteri kapatılıp kilitlenir. Motor çıkışlarında <a href="/post/motor-koruma-salteri-kilitleme">motor koruma şalteri</a>, saha tipi ayırıcılarda uygun <a href="/post/salter-kilidi-cesitleri">şalter kilidi</a> kullanılır.</li>
<li><b>Su hatları:</b> Giriş ve çıkış vanaları kapatılıp kilitlenir; HVAC hatlarında yaygın olan <a href="/post/kelebek-vana-kilitleme-ekipmanlari">kelebek vanalar</a> ve <a href="/post/küresel-vana-etiketleme-kilitleme-ürünleri">küresel vanalar</a> için uygun kilitler seçilir. Basınç tahliye edilir.</li>
<li><b>Mekanik enerji:</b> Fanın tamamen durduğu doğrulanır, gerekiyorsa fan çarkı veya kasnak sabitlenir.</li>
<li><b>Kilit ve etiket:</b> Her çalışan kendi kilidini takar; birden fazla nokta varsa <a href="/post/loto-kilit-kutusu-nasil-kullanilir">grup kilitleme kutusu</a> kullanılır. Kilitlere <a href="/eked-uyari-etiketleri">uyarı etiketi</a> asılır.</li>
<li><b>Doğrulama:</b> Yerel ve BMS üzerinden çalıştırma denenir; ekipman çalışmamalıdır.</li>
<li><b>Devreye alma:</b> İş bitince koruyucular takılır, herkes kendi kilidini çıkarır, vanalar kontrollü açılır ve ekipman BMS’te yeniden aktif edilir.</li>
</ol>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Ekipmanı sadece BMS’ten veya panelden durdurmak</li>
<li>Serbest dönen fanı hesaba katmamak</li>
<li>Kayış değiştirirken motor şalterini kilitlememek</li>
<li>Pompa veya eşanjör sökülürken vanaları kilitlememek ve basıncı tahliye etmemek</li>
<li>Dış firma (servis) ekibinin tesis kurallarını bilmemesi (bkz. <a href="/post/taseron-yuklenici-firmalarda-loto-uygulamasi">taşeron firmalarda LOTO</a>)</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-X07UN','LS-VN-02','LS-X02C']))}
<p>Benzer uygulamalar için <a href="/post/kompresor-bakiminda-loto">kompresör bakımında LOTO</a> ve <a href="/post/buhar-kazani-ve-buhar-hatlarinda-loto">buhar hatlarında LOTO</a> yazılarımıza göz atabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

P=[
 dict(slug='trafo-ve-og-hucre-bakiminda-loto', date='2026-11-02T09:10:00.000Z',
      title='Trafo ve OG Hücre Bakımında LOTO: 5 Güvenlik Kuralı ve Güvenli Kilitleme',
      seo_title='Trafo ve OG Hücre Bakımında LOTO, 5 Güvenlik Kuralı | Locksan Safety',
      desc='Trafo merkezi ve orta gerilim (OG) hücre bakımında LOTO (EKED) nasıl uygulanır? Elektrikte 5 güvenlik kuralı, ayırıcı kilitleme, AG tarafından geri besleme, topraklama ve gerekli ürünler.',
      faq=F1, body=B1, cover_lines=['Trafo ve OG','Hücre Bakımında','LOTO'], letter='OG', lab='TRAFO / OG HÜCRE', step='Uygulama Rehberi'),
 dict(slug='hvac-chiller-ve-klima-santrali-bakiminda-loto', date='2026-11-02T09:00:00.000Z',
      title='HVAC, Chiller ve Klima Santrali Bakımında LOTO: Otomatik Çalışmaya Karşı Kilitleme',
      seo_title='Chiller ve Klima Santrali (HVAC) Bakımında LOTO | Locksan Safety',
      desc='Chiller, klima santrali (AHU), fan ve pompa bakımında LOTO (EKED) nasıl uygulanır? BMS ile otomatik çalışma, serbest dönen fan, soğuk su hattı vana kilitleme; adımlar, hatalar ve ürünler.',
      faq=F2, body=B2, cover_lines=['Chiller ve Klima','Santrali Bakımında','LOTO'], letter='HVAC', lab='HVAC / CHILLER', step='Uygulama Rehberi'),
]
publish(P)
print('ok')
