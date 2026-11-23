import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from addpost import *

F1=[
 ('Elektrik panosu bakımında LOTO nasıl yapılır?','Önce panodan beslenen yükler normal yolla durdurulur, ardından panoyu besleyen üst şalter veya kesici açılıp uygun şalter kilitleme ekipmanı ve kişisel kilitle kilitlenir. Etiket asıldıktan sonra uygun ölçü aletiyle enerjisizlik doğrulanır; ancak bundan sonra pano kapağı açılarak çalışmaya başlanır.'),
 ('Pano içindeki ana şalteri kapatmak yeterli mi?','Çoğu zaman hayır. Ana şalterin giriş tarafındaki baralar ve klemensler hâlâ enerjilidir. Ayrıca panoda jeneratör, UPS, ikinci besleme veya harici kontrol gerilimi olabilir. Tüm besleme kaynakları belirlenip her biri ayrı ayrı izole edilmeli ve kilitlenmelidir.'),
 ('Enerjisizlik nasıl doğrulanır?','Gerilim, yetkili ve eğitimli bir elektrikçi tarafından uygun kategorideki ölçü aletiyle faz-faz ve faz-toprak arasında ölçülür. Ölçü aletinin çalıştığı ölçümden önce ve sonra bilinen bir kaynakta test edilir. Kondansatör ve sürücü bulunan panolarda üreticinin bekleme süresine uyulur.'),
 ('Pano kapağı kilitlenebilir mi?','Evet, pano kapağı veya pano odası girişi asma kilitle kilitlenebilir; ancak bu bir enerji izolasyonu değildir. Kapak kilidi yetkisiz erişimi engeller, asıl LOTO ise panoyu besleyen enerji kaynağının izolasyon noktasında yapılmalıdır.'),
 ('Birden fazla elektrikçi aynı panoda çalışıyorsa ne yapılır?','Her çalışan izolasyon noktasına kendi kişisel kilidini takar. Kilit sayısı fazlaysa kilit çoklayıcı kullanılır veya izolasyon anahtarları grup kilitleme kutusunda toplanır ve her çalışan kutuya kendi kilidini takar.'),
]
B1=f'''
<p>Dağıtım panoları, motor kontrol merkezleri (MCC), kompanzasyon ve otomasyon panoları bir tesisin elektrik altyapısının kalbidir. Klemens sıkma, kesici değişimi, termografi sonrası müdahale veya kablo ekleme gibi işlerde en büyük tehlike, <b>enerjisiz sanılan bir bölümde gerilim kalmasıdır</b>. İkinci besleme, jeneratör veya UPS dönüşü ve kondansatörlerde kalan enerji bu riskin en sık görülen kaynaklarıdır. Bu yazıda <b>elektrik panosu bakımında LOTO (EKED)</b> uygulamasını adım adım ele alıyoruz.</p>

<h2>Panoda Enerji Kaynakları ve Kontrolü</h2>
{table(['Kaynak','Nerede?','Risk','Kontrol'],[
 ['Ana besleme','Üst dağıtım panosu, trafo çıkışı','Giriş baralarında gerilim kalması','Üst kesiciyi kilitleme; <a href="/post/acik-tip-devre-kesici-acb-kilitleme">ACB</a> veya <a href="/post/kompakt-şalter-etiketleme-kilitleme-ürünleri">kompakt şalter</a> kilidi'],
 ['İkinci besleme / jeneratör','Transfer şalteri, yedek hat','Otomatik transfer ile panonun yeniden enerjilenmesi','<a href="/post/transfer-salteri-ats-kilitleme">Transfer şalteri (ATS) kilitleme</a>, jeneratörü devre dışı bırakma'],
 ['UPS ve akü','Kesintisiz güç çıkışları','Ana şalter kapalıyken devrelerin enerjili kalması','UPS çıkışını izole etme; <a href="/post/jenerator-ve-ups-bakiminda-loto">jeneratör ve UPS bakımında LOTO</a>'],
 ['Kontrol gerilimi','Harici 24V / 230V kumanda beslemesi','Kumanda devrelerinde beklenmeyen gerilim','Kumanda sigortalarını <a href="/post/minyatür-şalter-etiketleme-kilitleme-ürünleri">minyatür şalter kilidi</a> ile kilitleme'],
 ['Kalan enerji','Kompanzasyon kondansatörleri, sürücüler (VFD)','Kapatma sonrası elektrik çarpması','Bekleme süresi, deşarj ve ölçümle doğrulama'],
])}

<h2>Adım Adım Pano LOTO</h2>
<ol>
<li><b>Hazırlık:</b> Pano tek hat şeması üzerinden tüm besleme kaynakları (ana hat, yedek hat, jeneratör, UPS, harici kumanda gerilimi) belirlenir. Etkilenecek bölümler ve operatörler bilgilendirilir; iş <a href="/calisma-izni-ve-kilitleme-proseduru">çalışma izni ve kilitleme prosedürüne</a> bağlanır.</li>
<li><b>Yüklerin durdurulması:</b> Panodan beslenen makineler ve motorlar normal yolla durdurulur; yük altında şalter açılmaz.</li>
<li><b>İzolasyon:</b> Panoyu besleyen üst kesici veya şalter açılır. Yedek besleme ve transfer şalteri varsa onlar da açık konuma alınır.</li>
<li><b>Kilitleme:</b> Her izolasyon noktasına şalter tipine uygun <a href="/salter-kilitleme-ekipmanlari">şalter kilitleme ekipmanı</a> takılır ve çalışan kendi <a href="/emniyet-asma-kilitler">emniyet asma kilidini</a> kilitler. Seçim için <a href="/post/salter-kilidi-cesitleri">şalter kilidi çeşitleri</a> yazımıza bakabilirsiniz.</li>
<li><b>Etiketleme:</b> Kilitlerin yanına kilitleyen kişiyi, tarihi ve yapılan işi gösteren <a href="/eked-uyari-etiketleri">EKED uyarı etiketleri</a> asılır. Bkz. <a href="/post/etiketle-eked-etiketleme-adimi">Etiketle: etiketleme adımı</a>.</li>
<li><b>Kalan enerjinin giderilmesi:</b> Kondansatör ve sürücülerde üreticinin belirttiği bekleme süresine uyulur; gerekiyorsa yetkili kişi tarafından uygun yöntemle deşarj edilir.</li>
<li><b>Doğrulama:</b> Yetkili elektrikçi, uygun ölçü aletiyle giriş ve çıkış baralarında gerilim olmadığını ölçer. Ölçü aleti ölçümden önce ve sonra bilinen bir kaynakta test edilir. Bkz. <a href="/post/dene-eked-test-adimi">Dene: test adımı</a>.</li>
<li><b>Çalışma ve hizmete alma:</b> İş bitince aletler ve artıklar panodan alınır, kapaklar kapatılır, personel uzaklaştırılır. Kilitler sahipleri tarafından çıkarılır ve pano kontrollü şekilde enerjilendirilir.</li>
</ol>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Sadece pano içindeki ana şalteri kapatıp giriş baralarının enerjili olduğunu unutmak</li>
<li>Jeneratör, UPS veya ikinci besleme hattını izole etmemek</li>
<li>Kilit takmadan yalnızca “çalışma var” notu bırakmak</li>
<li>Gerilim ölçümü yapmadan veya çalışmayan bir ölçü aletine güvenerek işe başlamak</li>
<li>Pano kapağını kilitlemeyi enerji izolasyonu yerine saymak</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-EK-S1100VV','LS-X02-ELK-SET','LS-PE-E010S']))}
<p>Tüm şalter tipleri için <a href="/salter-kilitleme-ekipmanlari">şalter kilitleme ekipmanları</a>, ortak izolasyon noktaları için <a href="/coklandiricilar">çoklayıcılar</a> ve <a href="/grup-kilitleme-kutulari-ve-eked-cantalari">grup kilitleme kutuları</a> kategorilerimize göz atabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

F2=[
 ('Paketleme makinelerinde LOTO neden önemlidir?','Paketleme ve ambalaj makinelerinde sık sık sıkışma giderme, rulo film değişimi, format değişimi ve temizlik yapılır. Bu işlerde çalışanın eli kesici bıçak, mühürleme çenesi veya taşıyıcı zincir gibi tehlikeli bölgelere girer. Makinenin beklenmedik şekilde çalışmasını önlemenin güvenilir yolu enerji kaynaklarını izole edip kilitlemektir.'),
 ('Sıkışma giderirken acil stop basmak yeterli mi?','Hayır. Acil stop bir durdurma işlevidir, enerji izolasyonu değildir; resetlenince makine çalışmaya hazır hâle gelir ve pnömatik silindirlerde basınç kalabilir. Tehlikeli bölgeye girilecekse elektrik ve pnömatik enerji izole edilip kilitlenmelidir.'),
 ('Pnömatik enerji nasıl izole edilir?','Makine girişindeki pnömatik kapatma vanası kapatılıp kilitlenir veya hızlı bağlantı fişi sökülerek pnömatik fiş kilidi takılır. Ardından sistemdeki basınç tahliye edilir ve silindirlerin hareket etmediği kontrol edilir.'),
 ('Kısa süreli ayar işlerinde de kilitleme gerekir mi?','Tesisin risk değerlendirmesine ve prosedürüne bağlıdır. Tehlikeli bölgeye vücudun bir kısmının girdiği işlerde, süre kısa olsa bile, genel kural enerji izolasyonu ve kilitlemedir. Kilitlemenin uygulanmadığı istisnalar ancak prosedürde tanımlı ve eşdeğer koruma sağlayan önlemlerle yapılabilir.'),
 ('Hat şeklindeki paketleme sistemlerinde kilitleme nasıl organize edilir?','Dolum, kapama, etiketleme ve koli makinelerinden oluşan hatlarda her makinenin izolasyon noktaları ayrı ayrı belirlenir. Bakım birden fazla makineyi kapsıyorsa anahtarlar grup kilitleme kutusunda toplanır ve her çalışan kutuya kendi kilidini takar.'),
]
B2=f'''
<p>Dikey ve yatay form-dolum-mühürleme (VFFS / HFFS), flow-pack, streç sarma, koli kapama ve şrink makineleri gıda, ilaç, kozmetik ve kimya sektörlerinde vardiya boyunca durmadan çalışır. Bu makinelerde kazaların önemli bir kısmı üretim sırasında değil; <b>sıkışma giderme, film rulosu değişimi, format değişimi ve temizlik</b> sırasında olur. Çalışanın eli kesici bıçağa, sıcak mühürleme çenesine veya taşıyıcı zincire yaklaşırken makinenin bir anda çalışması ciddi yaralanmalara yol açabilir. Bu yazıda <b>paketleme ve ambalaj makinelerinde LOTO (EKED)</b> uygulamasını anlatıyoruz.</p>

<h2>Paketleme Makinelerinde Enerji Kaynakları</h2>
{table(['Enerji','Nerede?','Risk','Kontrol'],[
 ['Elektrik','Ana şalter, servo sürücüler, motorlar','Bıçak, çene veya taşıyıcının beklenmedik hareketi','Makine ana şalterini <a href="/salter-kilitleme-ekipmanlari">şalter kilidiyle</a> kilitleme'],
 ['Pnömatik','Kesme, itme ve mühürleme silindirleri','Silindirlerin basınçla ani hareketi','Pnömatik vanayı veya <a href="/post/fis-kilidi-elektrik-ve-pnomatik-fis-kilitleme">hızlı bağlantı fişini</a> kilitleme, basınç tahliyesi'],
 ['Termal','Mühürleme çeneleri, şrink tüneli','Yanık','Soğumayı bekleme, sıcaklığı kontrol etme'],
 ['Mekanik / yerçekimi','Askıdaki çeneler, film rulosu, kaldırılmış kapaklar','Düşme, sıkışma','Mekanik destekle sabitleme'],
 ['Gerilmiş film / yay','Film gergi kolları, streç sarma','Ani boşalma ile çarpma','Gerginliği kontrollü boşaltma'],
])}

<h2>Adım Adım Paketleme Makinesi LOTO</h2>
<ol>
<li><b>Hazırlık:</b> Makinenin tüm izolasyon noktaları (ana şalter, pnömatik giriş vanası, varsa vakum ve soğutma hatları) makine bazlı LOTO talimatında tanımlanır. Örnek için <a href="/post/loto-proseduru-ornegi">LOTO prosedürü örneği</a> yazımıza bakabilirsiniz.</li>
<li><b>Bilgilendirme ve durdurma:</b> Operatör ve hattaki diğer makinelerin sorumluları bilgilendirilir, makine normal yolla durdurulur.</li>
<li><b>Elektrik izolasyonu:</b> Ana şalter kapatılır, uygun kilitleme ekipmanı takılır ve kişisel kilit kilitlenir.</li>
<li><b>Pnömatik izolasyon:</b> Pnömatik giriş vanası kapatılıp kilitlenir veya hat fişi sökülüp fiş kilidi takılır. Sistemdeki basınç tahliye edilir. Ayrıntılar için <a href="/post/pnomatik-ve-hidrolik-sistemlerde-loto">pnömatik ve hidrolik sistemlerde LOTO</a> yazımıza bakabilirsiniz.</li>
<li><b>Kalan enerjinin kontrolü:</b> Mühürleme çenelerinin soğuması beklenir, askıdaki parçalar mekanik olarak desteklenir, film gerginliği boşaltılır.</li>
<li><b>Etiketleme:</b> İzolasyon noktalarına <a href="/eked-uyari-etiketleri">EKED uyarı etiketleri</a> asılır.</li>
<li><b>Doğrulama:</b> Makine kumanda panelinden çalıştırılmayı denenir, hiçbir hareket olmamalıdır. Pnömatik manometre sıfırı göstermelidir. Ardından kumanda tekrar kapalı konuma alınır. Bkz. <a href="/post/dene-eked-test-adimi">Dene: test adımı</a>.</li>
<li><b>Hizmete alma:</b> Sıkışan ürün ve aletler temizlenir, koruyucular ve kapaklar yerine takılır, çevre kontrol edilir. Kilitler sahipleri tarafından çıkarılır ve makine kontrollü şekilde devreye alınır.</li>
</ol>

<h2>Hatlarda ve Vardiyalarda Dikkat</h2>
<ul>
<li><b>Bağlantılı makineler:</b> Besleme konveyörü veya dolum makinesi çalışırken paketleme makinesine ürün gelmeye devam edebilir. Gerekiyorsa önceki makine de izole edilir; bkz. <a href="/post/konveyor-bakiminda-loto-nasil-uygulanir">konveyör bakımında LOTO</a>.</li>
<li><b>Çok kişili bakım:</b> Birden fazla teknisyen çalışıyorsa <a href="/post/kilit-coklayici-nedir-cesitleri">kilit çoklayıcı</a> veya <a href="/post/loto-kilit-kutusu-nasil-kullanilir">grup kilitleme kutusu</a> kullanılır.</li>
<li><b>Vardiya devri:</b> Bakım vardiya değişimine sarkıyorsa kilitler kontrollü şekilde devredilir; bkz. <a href="/post/vardiya-degisiminde-loto-devri">vardiya değişiminde LOTO devri</a>.</li>
<li><b>Gıda ve ilaç hatları:</b> Islak temizlik yapılan alanlarda kilit ve etiketlerin ortama uygunluğuna dikkat edilir; bkz. <a href="/post/gida-sektorunde-loto-eked">gıda sektöründe LOTO</a>.</li>
</ul>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Sıkışma giderirken yalnızca acil stop veya kumanda panelindeki durdurma butonuna güvenmek</li>
<li>Elektriği kilitleyip pnömatik basıncı tahliye etmemek</li>
<li>Kapak emniyet anahtarını (interlock) köprüleyerek makineye müdahale etmek</li>
<li>Sıcak mühürleme çenelerinin soğumasını beklememek</li>
<li>Hatta önceki makineden ürün beslemesinin devam ettiğini hesaba katmamak</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-PR-UV07','LS-PS02S','LS-X02CY']))}
<p>Pnömatik izolasyon için <a href="/pnomatik-baglanti-kilitleme-ekipmanlari">pnömatik bağlantı kilitleme ekipmanları</a>, elektriksel izolasyon için <a href="/salter-kilitleme-ekipmanlari">şalter kilitleme ekipmanları</a> kategorilerimize göz atabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

P=[
 dict(slug='paketleme-ve-ambalaj-makinelerinde-loto', date='2026-11-23T06:10:00.000Z',
      title='Paketleme ve Ambalaj Makinelerinde LOTO: Sıkışma, Format Değişimi ve Temizlik',
      seo_title='Paketleme ve Ambalaj Makinelerinde LOTO | Locksan Safety',
      desc='Paketleme ve ambalaj makinelerinde LOTO (EKED) nasıl uygulanır? Sıkışma giderme, film ve format değişiminde elektrik ve pnömatik kilitleme, adımlar, hatalar ve önerilen setler.',
      faq=F2, body=B2, cover_lines=['Paketleme','Makinelerinde','LOTO'], letter='PKT', lab='PAKETLEME', step='Uygulama Rehberi'),
 dict(slug='elektrik-panosu-bakiminda-loto', date='2026-11-23T06:00:00.000Z',
      title='Elektrik Panosu Bakımında LOTO: Besleme İzolasyonu, Kilitleme ve Gerilim Kontrolü',
      seo_title='Elektrik Panosu Bakımında LOTO Nasıl Yapılır? | Locksan Safety',
      desc='Elektrik panosu bakımında LOTO (EKED) nasıl yapılır? Ana ve yedek besleme izolasyonu, UPS ve jeneratör, şalter kilitleme, gerilim ölçümü ile doğrulama ve önerilen setler.',
      faq=F1, body=B1, cover_lines=['Elektrik Panosu','Bakımında','LOTO'], letter='PANO', lab='ELEKTRİK PANOSU', step='Uygulama Rehberi'),
]
publish(P)
print('ok')
