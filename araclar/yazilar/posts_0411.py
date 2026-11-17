import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from addpost import *

F1=[
 ('CNC tezgâh bakımında neden LOTO gerekir?','CNC tezgâhlarında iş mili, eksen motorları, takım magazini ve talaş konveyörü programla veya uzaktan otomatik hareket edebilir. Ayrıca hidrolik ayna, pnömatik takım bağlama ve soğutma sıvısı pompası gibi farklı enerji kaynakları bulunur. Bakım ve onarımda tüm bu enerjiler izole edilip kilitlenmelidir.'),
 ('Acil stop veya “feed hold” LOTO yerine geçer mi?','Hayır. Acil stop, feed hold ve kapı kilidi gibi düzenekler üretim sırasında koruma sağlar; enerji izolasyonu değildir. Bakım işlerinde ana şalter kilitlenmelidir.'),
 ('Takım değiştirmek için de LOTO gerekir mi?','Operatörün tezgâhın normal kullanımı sırasında, üreticinin öngördüğü koruma düzenekleriyle yaptığı rutin takım değişimi genellikle üretim işi kapsamındadır. Ancak takım magazini arızası, sıkışan takımın çıkarılması veya koruyucuların açılması gibi işlerde LOTO uygulanmalıdır.'),
 ('Hidrolik aynada nelere dikkat edilmeli?','Hidrolik ayna basınç kesilince iş parçasını bırakabilir; ağır parçalar düşebilir. Bakım öncesi parça güvenli şekilde sökülmeli, hidrolik ünite kapatılıp kilitlenmeli ve akümülatör basıncı tahliye edilmelidir.'),
 ('CNC tezgâhı için hangi LOTO ürünleri gerekir?','Ana şalter için şalter kilitleme ekipmanı veya doğrudan emniyet asma kilidi, hava hattı için küresel vana veya pnömatik bağlantı kilidi, çoklayıcı ve uyarı etiketleri temel ekipmanlardır.'),
]
B1=f'''
<p>Metal işleme atölyelerinin vazgeçilmezi olan <b>CNC torna, işleme merkezi ve freze tezgâhları</b>, yüksek devirli iş mili ve hızlı eksen hareketleriyle çalışır. Bu tezgâhların büyük çoğunluğu programla veya otomatik çevrimle hareket ettiği için, bakım sırasında yanlışlıkla başlatılan tek bir program ciddi yaralanmalara yol açabilir. Bu yazıda CNC tezgâh bakımında LOTO uygulamasını anlatıyoruz.</p>

<h2>CNC Tezgâhında Enerji Kaynakları</h2>
{table(['Enerji','Nerede?','Risk','Kontrol'],[
 ['Elektrik','Ana besleme, iş mili ve eksen motorları, kontrol ünitesi','Programla veya uzaktan hareket','<a href="/salter-kilitleme-ekipmanlari">Şalter kilidi</a> + kişisel kilit'],
 ['Hidrolik','Ayna, punta, kelepçe sistemleri','Parçanın bırakılması, sıkıştırma','Ünite kapatma + akümülatör tahliyesi'],
 ['Pnömatik','Takım bağlama, kapı silindirleri, üfleme','Ani hareket','<a href="/pnomatik-baglanti-kilitleme-ekipmanlari">Pnömatik kilit</a> + tahliye'],
 ['Mekanik / yerçekimi','Dikey eksen (Z) kafası, takım magazini','Eksenin düşmesi, sıkışma','Ekseni alt konuma alma, mekanik destek'],
 ['Diğer','Talaş konveyörü, soğutma sıvısı pompası','Kapılma, sıvı püskürmesi','Ana şalterle birlikte izolasyon'],
])}

<h2>Adım Adım CNC LOTO</h2>
<ol>
<li><b>Hazırlık:</b> Tezgâha özel prosedürde tüm enerji kaynakları ve izolasyon noktaları tanımlanır. Bkz. <a href="/post/loto-proseduru-ornegi">LOTO prosedürü örneği</a>.</li>
<li><b>Güvenli konum:</b> Program durdurulur, dikey eksen alt konuma alınır, iş parçası ve takım güvenli hale getirilir.</li>
<li><b>Elektrik izolasyonu:</b> Tezgâhın döner ana şalteri kapatılıp emniyet asma kilidiyle kilitlenir. Kilitleme deliği yoksa uygun <a href="/post/salter-kilidi-cesitleri">şalter kilidi</a> kullanılır.</li>
<li><b>Hidrolik ve pnömatik:</b> Hava beslemesi <a href="/ls-f01d-ayarlanabilir-kuresel-vana-kilitleme">küresel vana kilidiyle</a> kilitlenir, hidrolik ünite kapatılır, basınçlar tahliye edilir. Bkz. <a href="/post/pnomatik-ve-hidrolik-sistemlerde-loto">pnömatik ve hidrolik LOTO</a>.</li>
<li><b>Kilit ve etiket:</b> Her çalışan kendi kilidini takar; birden fazla kişi varsa <a href="/coklandiricilar">çoklayıcı</a> kullanılır. Kilitlere <a href="/eked-uyari-etiketleri">uyarı etiketi</a> asılır.</li>
<li><b>Doğrulama:</b> Kontrol panelinden açma ve hareket denenir; tezgâh çalışmamalıdır. Bkz. <a href="/post/dene-eked-test-adimi">Dene: test adımı</a>.</li>
<li><b>Bakım ve devreye alma:</b> İş bitince koruyucular takılır, alan temizlenir, herkes kendi kilidini çıkarır ve tezgâh referans alınarak düşük hızda test edilir.</li>
</ol>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Acil stop butonuna basıp tezgâhın içine girmek</li>
<li>Kapı emniyet şalterini köprüleyerek çalışmak</li>
<li>Hidrolik aynayı basınç tahliye etmeden sökmek</li>
<li>Talaş konveyörünü çalışırken temizlemek</li>
<li>Dikey ekseni desteklemeden fren veya motor üzerinde çalışmak</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-X02C','LS-X07UN','LS-PS02S']))}
<p>Benzer makineler için <a href="/post/pres-makinelerinde-loto-ve-kalip-degisimi">pres makinelerinde LOTO</a> ve <a href="/post/robot-hucrelerinde-loto">robot hücrelerinde LOTO</a> yazılarımıza göz atabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

F2=[
 ('Kapalı alanda çalışırken LOTO neden gereklidir?','Tank, silo, kuyu, kanal ve kazan gibi kapalı alanlarda içerideki çalışanın en büyük risklerinden biri, ekipmanın çalışması veya alana madde, gaz ya da su girmesidir. Karıştırıcılar, pompalar ve besleme hatları kilitlenmeden kapalı alana girilmemelidir.'),
 ('Kapalı alan nedir?','Giriş ve çıkışı sınırlı, sürekli çalışma için tasarlanmamış ve tehlikeli atmosfer oluşabilecek alanlardır. Tanklar, silolar, reaktörler, kuyular, kanalizasyon ve büyük borular tipik örneklerdir.'),
 ('Kapalı alanda boru hatları nasıl izole edilir?','Alana giren tüm hatlar körtapa (kör flanş) takılarak, hattın bir bölümü sökülerek veya çift vana arası tahliye yöntemiyle izole edilir. Vanalar kilitlenir ve etiketlenir. Sadece tek vanayı kapatmak çoğu durumda yeterli kabul edilmez.'),
 ('LOTO yapıldıysa ortam ölçümüne gerek var mı?','Evet. LOTO enerji ve madde girişini engeller ama içerideki atmosferi güvenli yapmaz. Girişten önce ve çalışma boyunca oksijen, yanıcı gaz ve zehirli gaz ölçümü yapılmalıdır.'),
 ('Kapalı alan girişinde hangi ekipmanlar gerekir?','LOTO için şalter ve vana kilitleri, grup kilitleme kutusu, çoklayıcı, emniyet asma kilitleri ve uyarı etiketleri; kapalı alan için ise gaz dedektörü, havalandırma ekipmanı, emniyet kemeri ve kurtarma ekipmanı gerekir.'),
]
B2=f'''
<p><b>Kapalı alan çalışmaları</b> (tank, silo, reaktör, kuyu, kanal temizliği ve bakımı), iş kazalarında ölüm oranının en yüksek olduğu işler arasındadır. Bu kazaların bir kısmı zehirli veya oksijensiz atmosferden, önemli bir kısmı ise içeride biri varken <b>bir karıştırıcının çalışması, bir pompanın devreye girmesi ya da hatta sıvı veya gaz gelmesinden</b> kaynaklanır. Bu yazıda kapalı alan girişinde LOTO’nun rolünü ve uygulama adımlarını anlatıyoruz.</p>

<h2>Kapalı Alanda Hangi Enerjiler İzole Edilir?</h2>
{table(['Kaynak','Örnek','Risk','İzolasyon'],[
 ['Elektrik','Karıştırıcı, pompa, helezon, ısıtıcı','Kapılma, ezilme, yanık','<a href="/salter-kilitleme-ekipmanlari">Şalter kilidi</a>'],
 ['Proses hatları','Hammadde, buhar, su, gaz hatları','Boğulma, yanık, zehirlenme','Körtapa, hat ayırma veya çift vana + tahliye, <a href="/vana-kilitleme-ekipmanlari">vana kilidi</a>'],
 ['Pnömatik / hidrolik','Vana aktüatörleri, kapaklar','Ani hareket','Besleme kilitleme + tahliye'],
 ['Yerçekimi / malzeme','Silo ve bunker içindeki ürün','Gömülme','Boşaltma ekipmanlarını kilitleme'],
 ['Isıl','Ceketli tanklar, buhar serpantinleri','Yanık','Soğuma bekleme'],
])}

<h2>Adım Adım Kapalı Alan LOTO</h2>
<ol>
<li><b>Çalışma izni:</b> Kapalı alan giriş izni düzenlenir; izin formunda tüm izolasyon noktaları listelenir. Bkz. <a href="/calisma-izni-ve-kilitleme-proseduru">çalışma izni ve kilitleme prosedürü</a>.</li>
<li><b>Boşaltma ve temizleme:</b> Alan boşaltılır, gerekiyorsa yıkanır veya inert gazla temizlenir.</li>
<li><b>Hat izolasyonu:</b> Alana giren tüm hatlar körtapa ile kapatılır, ayrılır veya çift vana arası tahliye ile izole edilir. Vanalar kilitlenir. Bkz. <a href="/post/vana-valf-kilitleme-rehberi">vana ve valf kilitleme rehberi</a>.</li>
<li><b>Elektrik izolasyonu:</b> Karıştırıcı, pompa ve ısıtıcıların şalterleri kapatılıp kilitlenir.</li>
<li><b>Grup kilitleme:</b> İzolasyon kilitlerinin anahtarları <a href="/post/loto-kilit-kutusu-nasil-kullanilir">grup kilitleme kutusuna</a> konur; içeri girecek her çalışan ve gözcü kendi kişisel kilidini takar.</li>
<li><b>Doğrulama:</b> Ekipmanlar çalıştırılmayı denenir, hatlarda basınç ve akış olmadığı kontrol edilir.</li>
<li><b>Atmosfer ölçümü:</b> Oksijen, yanıcı ve zehirli gaz ölçülür; havalandırma sağlanır. Ölçüm çalışma boyunca sürdürülür.</li>
<li><b>Giriş ve çıkış:</b> Gözcü ve kurtarma planı hazırken giriş yapılır. İş bitince herkes çıkar, sayım yapılır ve kilitler sahipleri tarafından çıkarılır.</li>
</ol>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Sadece karıştırıcıyı kilitleyip proses hatlarını unutmak</li>
<li>Tek vanayı kapatıp körtapa veya tahliye yapmamak</li>
<li>LOTO yapıldı diye ortam ölçümünü atlamak</li>
<li>İçeri giren çalışanın kendi kilidini takmaması</li>
<li>Vardiya değişiminde kilitlerin devri yapılmadan ayrılmak</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-8812S','LS-VN-02','LS-GKV-S500']))}
<p>Uygulama örnekleri için <a href="/post/silo-ve-bunker-bakiminda-loto">silo ve bunker bakımında LOTO</a>, <a href="/post/atik-su-aritma-tesislerinde-loto">arıtma tesislerinde LOTO</a> ve <a href="/post/kimya-ve-petrokimya-tesislerinde-loto">kimya tesislerinde LOTO</a> yazılarımıza bakabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

P=[
 dict(slug='kapali-alan-calismalarinda-loto', date='2026-11-04T09:10:00.000Z',
      title='Kapalı Alan Çalışmalarında LOTO: Tank, Silo ve Kuyu Girişinde Güvenli İzolasyon',
      seo_title='Kapalı Alan Çalışmalarında LOTO ve Enerji İzolasyonu | Locksan Safety',
      desc='Tank, silo, reaktör ve kuyu gibi kapalı alanlara girişte LOTO (EKED) nasıl uygulanır? Karıştırıcı ve pompa kilitleme, körtapa ve çift vana ile hat izolasyonu, grup kilitleme ve ortam ölçümü.',
      faq=F2, body=B2, cover_lines=['Kapalı Alan','Çalışmalarında','LOTO'], letter='TANK', lab='KAPALI ALAN', step='Uygulama Rehberi'),
 dict(slug='cnc-tezgah-bakiminda-loto', date='2026-11-04T09:00:00.000Z',
      title='CNC Tezgâh Bakımında LOTO: Torna, İşleme Merkezi ve Freze İçin Güvenli Kilitleme',
      seo_title='CNC Tezgâh Bakımında LOTO ve İş Güvenliği | Locksan Safety',
      desc='CNC torna, işleme merkezi ve freze bakımında LOTO (EKED) nasıl uygulanır? İş mili ve eksen motorları, hidrolik ayna, pnömatik takım bağlama, dikey eksen riskleri; adımlar ve gerekli ürünler.',
      faq=F1, body=B1, cover_lines=['CNC Tezgâh','Bakımında','LOTO'], letter='CNC', lab='CNC TEZGÂH', step='Uygulama Rehberi'),
]
publish(P)
print('ok')
