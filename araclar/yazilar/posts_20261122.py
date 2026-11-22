import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from addpost import *

F1=[
 ('Pompa bakımında LOTO nasıl uygulanır?','Önce pompa normal yolla durdurulur, motorun beslendiği şalter veya motor koruma şalteri kapatılıp kilitlenir. Ardından emme ve basma vanaları kapatılıp vana kilitleme ekipmanlarıyla kilitlenir, pompa gövdesindeki basınç ve sıvı tahliye edilir. Son olarak pompa çalıştırılmayı denenir ve basınç göstergesi kontrol edilir.'),
 ('Sadece pompa motorunu kilitlemek yeterli mi?','Hayır. Motor kilitlense bile hatta kalan basınç, akışkanın geri akışı veya sıcak akışkan pompa açıldığında çalışanı yaralayabilir. Elektrik izolasyonunun yanında emme ve basma vanaları da kilitlenmeli, gövde basıncı tahliye edilmelidir.'),
 ('Pompa geri akışla dönebilir mi?','Evet. Basma hattındaki çekvalf sızdırıyorsa veya hiç yoksa, hattaki akışkan geri akarak pompa çarkını ters yönde döndürebilir. Bu yüzden basma vanası kapatılıp kilitlenmeli, çekvalfe tek başına güvenilmemelidir.'),
 ('Frekans invertörlü pompalarda nelere dikkat edilmeli?','Sürücü (VFD) kapatıldıktan sonra içindeki kondansatörlerde bir süre enerji kalabilir. İzolasyon sürücünün beslemesinden yapılmalı, üreticinin belirttiği bekleme süresine uyulmalı ve enerjisizlik uygun ölçü aletiyle doğrulanmalıdır.'),
 ('Paralel çalışan pompalardan biri nasıl izole edilir?','Ortak kollektöre bağlı pompalarda diğer pompa çalışmaya devam ettiği için hat basınç altındadır. Bakıma alınacak pompanın kendi emme ve basma vanaları kapatılıp kilitlenir, motoru ayrıca kilitlenir ve otomatik devreye alma (yedek pompa) mantığı bu pompa için devre dışı bırakılır.'),
]
B1=f'''
<p>Santrifüj, dişli, dalgıç veya dozaj pompası fark etmez: <b>pompalar</b> neredeyse her tesiste su, kimyasal, yakıt, yağ ve proses akışkanlarını taşır. Salmastra, mekanik conta, rulman veya çark değişimi gibi bakımlarda tehlike sadece motorun çalışması değildir; hatta kalan <b>basınç</b>, <b>sıcak veya kimyasal akışkan</b> ve <b>geri akış</b> da ciddi yaralanmalara yol açabilir. Bu yazıda pompa bakımında LOTO (EKED) uygulamasını adım adım anlatıyoruz.</p>

<h2>Pompada Enerji Kaynakları</h2>
{table(['Enerji','Nerede?','Risk','Kontrol'],[
 ['Elektrik','Pompa motoru, sürücü (VFD), kontrol panosu','Pompanın beklenmedik çalışması, elektrik çarpması','<a href="/post/motor-koruma-salteri-kilitleme">Motor koruma şalteri</a> veya pano şalterini kilitleme'],
 ['Hidrolik (akışkan basıncı)','Emme ve basma hatları, pompa gövdesi','Flanş veya kapak açılırken akışkan fışkırması','Emme ve basma vanalarını kilitleme, basınç tahliyesi'],
 ['Geri akış / yerçekimi','Basma hattı, yüksekteki tanklar','Çarkın ters dönmesi, hattın dolması','Basma vanasını kilitleme; <a href="/post/cekvalf-kilitleme-loto">çekvalfe</a> tek başına güvenmeme'],
 ['Termal','Sıcak su, buhar kondensi, kızgın yağ pompaları','Yanık','Soğumayı bekleme, sıcaklığı ölçme'],
 ['Kimyasal','Asit, kostik, solvent ve yakıt pompaları','Yanık, zehirlenme, yangın','Hattı boşaltma ve yıkama, uygun KKD'],
 ['Mekanik','Kaplin, mil, kayış-kasnak','Sıkışma, kesilme','Elektrik izolasyonu sonrası dönmediğini doğrulama'],
])}

<h2>Adım Adım Pompa LOTO</h2>
<ol>
<li><b>Hazırlık:</b> Bakıma alınacak pompa, beslediği hat ve tüm izolasyon noktaları (şalter, emme vanası, basma vanası, drenaj ve hava alma noktaları) belirlenir. Etkilenecek operatörler bilgilendirilir.</li>
<li><b>Normal durdurma:</b> Pompa kontrol panelinden veya proses sisteminden normal yolla durdurulur. Yedek pompa otomatik devreye girecek şekilde ayarlıysa bu durum dikkate alınır.</li>
<li><b>Elektrik izolasyonu:</b> Motorun beslendiği şalter kapatılır ve uygun <a href="/salter-kilitleme-ekipmanlari">şalter kilitleme ekipmanıyla</a> kişisel kilit takılır. Sürücülü (VFD) sistemlerde izolasyon sürücü beslemesinden yapılır ve üreticinin bekleme süresine uyulur.</li>
<li><b>Emme ve basma vanaları:</b> Her iki vana kapatılır ve tipine uygun ekipmanla kilitlenir: <a href="/post/küresel-vana-etiketleme-kilitleme-ürünleri">küresel vana</a>, <a href="/post/kelebek-vana-kilitleme-ekipmanlari">kelebek vana</a> veya <a href="/post/sürgü-simit-vana-etiketleme-kilitleme-ürünleri">sürgülü (simit) vana</a> kilitleri. Seçim için <a href="/post/vana-valf-kilitleme-rehberi">vana kilitleme rehberine</a> bakabilirsiniz.</li>
<li><b>Basınç tahliyesi ve boşaltma:</b> Pompa gövdesindeki drenaj ve hava alma vanaları kontrollü şekilde açılarak basınç ve akışkan tahliye edilir. Tahliye edilen akışkan güvenli şekilde toplanır; drenaj vanası iş süresince açık konumda kilitlenebilir.</li>
<li><b>Etiketleme:</b> Şalter ve vanalara kimin, neden ve ne zaman kilitlediğini gösteren <a href="/eked-uyari-etiketleri">EKED uyarı etiketleri</a> asılır.</li>
<li><b>Doğrulama:</b> Pompa yerinden ve panodan çalıştırılmayı denenir, çalışmamalıdır. Basınç göstergesi sıfırı göstermeli, drenajdan akış kesilmelidir. Ardından kontroller tekrar “kapalı” konuma alınır. Bkz. <a href="/post/dene-eked-test-adimi">Dene: test adımı</a>.</li>
<li><b>Hizmete alma:</b> İş bitince alan temizlenir, kaplin muhafazaları takılır, drenajlar kapatılır. Kilitler sahipleri tarafından çıkarılır, vanalar sırasıyla açılır ve pompa kontrollü şekilde devreye alınır.</li>
</ol>

<h2>Özel Durumlar</h2>
<ul>
<li><b>Paralel ve yedekli pompalar:</b> Diğer pompa çalışırken ortak kollektör basınç altındadır. Bakımdaki pompanın kendi vanaları mutlaka kilitlenmelidir.</li>
<li><b>Dalgıç pompalar:</b> Pompa kuyudan veya rögardan çıkarılmadan önce besleme şalteri kilitlenir; kablo ve fişli bağlantılarda <a href="/post/fis-kilidi-elektrik-ve-pnomatik-fis-kilitleme">fiş kilidi</a> kullanılabilir. Atık su uygulamaları için <a href="/post/atik-su-aritma-tesislerinde-loto">arıtma tesislerinde LOTO</a> yazımıza bakabilirsiniz.</li>
<li><b>Kimyasal ve dozaj pompaları:</b> Hat boşaltılıp yıkanmadan flanş açılmaz; kimyasala uygun KKD kullanılır. Bkz. <a href="/post/kimya-ve-petrokimya-tesislerinde-loto">kimya tesislerinde LOTO</a>.</li>
<li><b>Çok kişili bakım:</b> Birden fazla çalışan varsa izolasyon anahtarları <a href="/post/loto-kilit-kutusu-nasil-kullanilir">grup kilitleme kutusunda</a> toplanır veya <a href="/post/kilit-coklayici-nedir-cesitleri">kilit çoklayıcı</a> kullanılır.</li>
</ul>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Sadece motoru kilitleyip emme ve basma vanalarını açık bırakmak</li>
<li>Basma hattındaki çekvalfe güvenip basma vanasını kapatmamak</li>
<li>Gövde basıncını tahliye etmeden salmastra veya kapak cıvatalarını sökmek</li>
<li>Yedek pompanın otomatik devreye alma mantığını unutmak</li>
<li>Sıcak akışkan pompalarında soğumayı beklemeden müdahale etmek</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-VM-K05','LS-VN-02','LS-X02C']))}
<p>Vana kilitleme ürünleri için <a href="/vana-kilitleme-ekipmanlari">vana kilitleme ekipmanları</a>, elektriksel izolasyon için <a href="/salter-kilitleme-ekipmanlari">şalter kilitleme ekipmanları</a> kategorilerimize göz atabilirsiniz. İhtiyacınız olan ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

F2=[
 ('Kör flanş kilitleme nedir?','Kör flanş kilitleme, boru hattına takılan kör flanşın bağlantı cıvata veya somunlarının üzerini kapatarak flanşın yetkisiz kişilerce sökülmesini önleyen bir LOTO uygulamasıdır. Ekipman emniyet asma kilidiyle kilitlenir ve üzerine uyarı etiketi asılır.'),
 ('Kör flanş ile vana izolasyonu arasındaki fark nedir?','Vana kapatıldığında iç sızdırmazlık zamanla bozulabilir ve akışkan geçebilir. Kör flanş ise hattı fiziksel olarak kapatır. Bu nedenle tehlikeli akışkanlar, kapalı alana giriş veya sıcak işler öncesinde kör flanşla hat körleme daha güvenilir bir izolasyon yöntemi olarak tercih edilir.'),
 ('Kör flanş takarken hat nasıl hazırlanır?','Önce izolasyon vanaları kapatılıp kilitlenir, hattaki basınç ve akışkan tahliye edilir, gerekiyorsa hat yıkanır veya inert gazla süpürülür. Ancak bundan sonra flanş açılıp kör flanş veya körleme plakası yerleştirilir.'),
 ('Kör flanş kilitleme ekipmanı her flanşa uyar mı?','Ayarlanabilir modeller farklı somun ve cıvata ölçülerine uyum sağlayacak şekilde tasarlanır. Yine de seçim yapmadan önce flanş çapı, cıvata sayısı ve somun ölçüsü kontrol edilmeli, ürünün teknik bilgilerine bakılmalıdır.'),
 ('Kör flanş noktaları nasıl takip edilir?','Her körleme noktası numaralandırılır, bir körleme listesine veya çalışma izni formuna işlenir ve üzerine etiket asılır. İş bitiminde tüm kör flanşların listeye göre söküldüğü kontrol edilmeden hat devreye alınmaz.'),
]
B2=f'''
<p>Kimya, petrokimya, enerji ve su tesislerinde bazı işler için vananın kapatılıp kilitlenmesi yeterli görülmez. Tanka veya kapalı alana giriş, sıcak işler ya da tehlikeli akışkan taşıyan hatlarda bakım öncesi hat çoğu zaman <b>kör flanşla fiziksel olarak körlenir</b>. Kör flanşın da en az vana kadar güvence altına alınması gerekir; aksi halde iş sürerken biri flanşı söküp hattı açabilir. Bu yazıda <b>kör flanş kilitleme</b> ekipmanlarını ve boru hattı izolasyonunda nasıl kullanıldıklarını anlatıyoruz.</p>

<h2>Boru Hattı İzolasyon Yöntemleri</h2>
{table(['Yöntem','Nasıl yapılır?','Güvence seviyesi','Kilitleme'],[
 ['Tek vana izolasyonu','Tek bir vana kapatılır','Daha düşük; vana iç kaçak yapabilir','<a href="/post/vana-valf-kilitleme-rehberi">Vana kilitleme ekipmanı</a>'],
 ['Çift blok ve tahliye','İki vana kapatılır, aradaki tahliye vanası açılır','Daha yüksek','Üç vananın da kilitlenmesi'],
 ['Kör flanş / körleme plakası','Flanş açılıp hatta kör flanş veya plaka yerleştirilir','Yüksek; hat fiziksel olarak kapalıdır','<a href="/ls-fl01-fl02-fl03-kor-flans-kilitleme-ekipmani">Kör flanş kilitleme ekipmanı</a>'],
 ['Hat ayırma','Boru parçası (makara) sökülür, uçlar körlenir','Yüksek','Kör flanşların kilitlenmesi ve etiketlenmesi'],
])}
<p>Hangi yöntemin kullanılacağı akışkanın türüne, basınca, sıcaklığa ve yapılacak işe göre tesisin risk değerlendirmesi ve prosedürüyle belirlenir.</p>

<h2>Kör Flanş Kilitleme Ekipmanı Ne İşe Yarar?</h2>
<p>Kör flanş kilitleme ekipmanı, flanşı bağlayan cıvata ve somunların üzerini kapatarak anahtarla sökülmelerini engeller. Ekipman bir <a href="/emniyet-asma-kilitler">emniyet asma kilidi</a> ile kilitlenir; kilidin anahtarı izolasyonu yapan kişide kalır. Böylece kör flanş, çalışma bitip yetkili kişi kilidi çıkarana kadar yerinde kalır. Ayarlanabilir modellerimiz için <a href="/ls-fl01-fl02-fl03-kor-flans-kilitleme-ekipmani">LS-FL01 / FL02 / FL03 kör flanş kilitleme ekipmanı</a> sayfasına bakabilirsiniz.</p>

<h2>Adım Adım Kör Flanşla Hat İzolasyonu</h2>
<ol>
<li><b>Planlama:</b> Körlenecek noktalar P&amp;ID veya hat şeması üzerinde işaretlenir, her nokta numaralandırılıp bir körleme listesine yazılır. İş <a href="/calisma-izni-ve-kilitleme-proseduru">çalışma izni ve kilitleme prosedürüne</a> bağlanır.</li>
<li><b>Vana izolasyonu:</b> Hattı besleyen vanalar kapatılır ve kilitlenir. Bu, flanş açılırken akışkan gelmesini önler.</li>
<li><b>Basınç tahliyesi ve temizleme:</b> Hat drenaj ve hava alma noktalarından boşaltılır; gerekiyorsa yıkanır veya inert gazla süpürülür. Basıncın sıfır olduğu gösterge ile doğrulanır.</li>
<li><b>Körleme:</b> Flanş açılır, basınç sınıfına ve flanş ölçüsüne uygun kör flanş veya körleme plakası yeni conta ile yerleştirilip cıvatalar sıkılır.</li>
<li><b>Kilitleme:</b> Kör flanş kilitleme ekipmanı cıvata/somunların üzerine takılır ve kişisel kilitle kilitlenir. Çok kişili işlerde anahtarlar <a href="/grup-kilitleme-kutulari-ve-eked-cantalari">grup kilitleme kutusunda</a> toplanır.</li>
<li><b>Etiketleme:</b> Her körleme noktasına numarası, kilitleyen kişi ve tarih bilgisini taşıyan <a href="/eked-uyari-etiketleri">uyarı etiketi</a> asılır.</li>
<li><b>Doğrulama:</b> Hat tarafında basınç ve sızıntı kontrolü yapılır; gerekiyorsa gaz ölçümü yapılır. Kapalı alana giriş öncesi ölçümler için <a href="/post/kapali-alan-calismalarinda-loto">kapalı alan çalışmalarında LOTO</a> yazımıza bakabilirsiniz.</li>
<li><b>Kaldırma:</b> İş bitince körleme listesi tek tek kontrol edilerek tüm kör flanşlar sökülür, normal contalarla flanş bağlantıları yapılır ve hat kontrollü şekilde devreye alınır.</li>
</ol>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Kör flanşı takıp cıvataları kilitlememek ve etiketlememek</li>
<li>Körleme listesi tutmamak; iş sonunda bir kör flanşı hatta unutmak</li>
<li>Basınç sınıfına uygun olmayan ince plaka kullanmak</li>
<li>Hattı boşaltıp basıncı doğrulamadan flanşı açmak</li>
<li>Sadece kapalı vanaya güvenerek tehlikeli akışkan hattında çalışmak</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-VN-02','LS-GKV-S500','LS-8812S']))}
<p>Vana tiplerine göre kilitleme çözümleri için <a href="/vana-kilitleme-ekipmanlari">vana kilitleme ekipmanları</a> kategorimize, proses tesislerindeki genel uygulamalar için <a href="/post/kimya-ve-petrokimya-tesislerinde-loto">kimya ve petrokimya tesislerinde LOTO</a> ve <a href="/post/buhar-kazani-ve-buhar-hatlarinda-loto">buhar hatlarında LOTO</a> yazılarımıza göz atabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

P=[
 dict(slug='kor-flans-kilitleme-boru-hatti-izolasyonu', date='2026-11-22T06:10:00.000Z',
      title='Kör Flanş Kilitleme: Boru Hattı İzolasyonunda Körleme ve LOTO',
      seo_title='Kör Flanş Kilitleme ve Boru Hattı İzolasyonu | Locksan Safety',
      desc='Kör flanş kilitleme nedir, ne zaman gerekir? Tek vana, çift blok ve tahliye ile kör flanş izolasyonu farkı, adım adım hat körleme, körleme listesi ve önerilen LOTO ürünleri.',
      faq=F2, body=B2, cover_lines=['Kör Flanş','Kilitleme ve','Hat İzolasyonu'], letter='FL', lab='KÖR FLANŞ', step='Ürün Rehberi'),
 dict(slug='pompa-bakiminda-loto', date='2026-11-22T06:00:00.000Z',
      title='Pompa Bakımında LOTO: Motor, Emme ve Basma Vanası Kilitleme',
      seo_title='Pompa Bakımında LOTO Nasıl Uygulanır? | Locksan Safety',
      desc='Pompa bakımında LOTO (EKED) nasıl yapılır? Motor şalteri, emme ve basma vanası kilitleme, basınç tahliyesi, geri akış riski, VFD ve paralel pompalar; adımlar ve önerilen setler.',
      faq=F1, body=B1, cover_lines=['Pompa','Bakımında','LOTO'], letter='PMP', lab='POMPA', step='Uygulama Rehberi'),
]
publish(P)
print('ok')
