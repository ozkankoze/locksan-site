import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from addpost import *

F1=[
 ('GES bakımında neden LOTO gerekir?','Güneş panelleri ışık aldığı sürece DC gerilim üretir ve bu enerji kaynağı “kapatılamaz”. İnverter, DC birleştirici (combiner) kutuları ve AC panolarda çalışırken izolasyon noktalarının kilitlenmesi, panellerden ve şebekeden gelebilecek enerjiye karşı tek güvenli yöntemdir.'),
 ('Gece çalışmak DC tarafı güvenli yapar mı?','Hayır, tek başına yeterli değildir. Ay ışığı veya aydınlatma bile düşük de olsa gerilim oluşturabilir; ayrıca hava aydınlandığında gerilim hızla yükselir. DC ayırıcılar her durumda açılıp kilitlenmeli ve gerilim ölçülerek doğrulanmalıdır.'),
 ('DC ayırıcı yük altında açılabilir mi?','DC akımda ark söndürmek zordur. Uygulamada önce inverter AC tarafından veya kendi kontrolünden durdurulur, ardından yük altında açmaya uygun DC ayırıcı açılır. Konnektörler (MC4 vb.) yük altında kesinlikle çıkarılmamalıdır. Üretici talimatı esas alınmalıdır.'),
 ('İnverter kapatılınca hemen çalışılabilir mi?','Hayır. İnverter içindeki kondansatörler kapatıldıktan sonra bir süre gerilim tutar. Üreticinin belirttiği bekleme süresi beklenmeli ve ölçüm cihazıyla gerilimin olmadığı doğrulanmalıdır.'),
 ('GES için hangi LOTO ürünleri gerekir?','AC panolardaki kompakt ve minyatür şalterler için şalter kilitleri, DC ayırıcılar için uygun döner şalter kilitleri, sigortalı kutular için sigorta kilitleri, emniyet asma kilitleri, çoklayıcılar ve uyarı etiketleri temel ekipmanlardır.'),
]
B1=f'''
<p><b>Güneş enerjisi santralleri (GES)</b> ve çatı tipi güneş sistemleri hızla yaygınlaşıyor. Ancak bu sistemlerde bakım yapan teknisyenler, alışılmış elektrik işlerinden farklı bir riskle karşılaşır: <b>Paneller ışık aldığı sürece gerilim üretir</b> ve bu kaynağı bir şalterle “kapatmak” mümkün değildir. Bu yazıda GES bakımında LOTO (EKED) uygulamasını adım adım anlatıyoruz.</p>

<h2>GES’te Enerji Kaynakları ve Riskler</h2>
{table(['Bölüm','Enerji','Risk','Kontrol'],[
 ['PV paneller ve dizeler (string)','DC gerilim (gün ışığında sürekli)','Elektrik çarpması, DC ark','DC ayırıcı / sigorta izolasyonu + kilit'],
 ['DC birleştirici (combiner) kutusu','Birden çok dizinin DC gerilimi','Paralel kaynaklardan geri besleme','Tüm dizilerin sigorta/ayırıcısını açma'],
 ['İnverter','DC giriş, AC çıkış, kondansatörler','Kapatıldıktan sonra kalan gerilim','İki taraftan izolasyon + bekleme süresi'],
 ['AC pano / trafo','Şebeke ve inverter beslemesi','Şebekeden veya inverterden besleme','<a href="/salter-kilitleme-ekipmanlari">Şalter kilidi</a>'],
 ['Depolama (batarya)','DC depolanmış enerji','Yüksek akım, ark','Batarya ayırıcısını kilitleme'],
])}

<h2>Neden “Şalteri Kapattım” Yeterli Değil?</h2>
<p>Klasik bir panoda ana şalteri kapatıp kilitlediğinizde enerji kesilir. GES’te ise enerji <b>iki yönden</b> gelir: Bir yanda şebeke (AC), diğer yanda paneller (DC). Ayrıca batarya varsa üçüncü bir kaynak oluşur. Bu nedenle tüm kaynakların ayrı ayrı belirlenip kilitlenmesi gerekir. Konuya genel bakış için <a href="/post/enerji-izolasyonu-nedir">enerji izolasyonu nedir</a> yazımıza bakabilirsiniz.</p>

<h2>Adım Adım GES LOTO</h2>
<ol>
<li><b>Planlama:</b> Tek hat şeması üzerinden çalışılacak bölümü besleyen tüm DC dizileri, inverterler, AC şalterler ve varsa bataryalar listelenir.</li>
<li><b>İnverteri durdurma:</b> İnverter kendi kontrolünden veya AC çıkış şalterinden durdurulur; böylece DC devrede yük akımı kesilir.</li>
<li><b>AC izolasyonu:</b> İnverter AC çıkış şalteri ve gerekiyorsa pano girişleri kapatılıp kilitlenir. Panodaki şalter tipine göre <a href="/post/kompakt-şalter-etiketleme-kilitleme-ürünleri">kompakt şalter</a> veya <a href="/post/minyatür-şalter-etiketleme-kilitleme-ürünleri">minyatür şalter</a> kilidi kullanılır.</li>
<li><b>DC izolasyonu:</b> DC ayırıcılar açılıp kilitlenir; combiner kutusunda dizi sigortaları çıkarılır veya <a href="/ls-d11nx/kelepceli-sigorta-kilitleme-ekipmani">sigorta kilitleme ekipmanıyla</a> kilitlenir. Döner tip DC ayırıcılarda uygun <a href="/post/salter-kilidi-cesitleri">şalter kilidi</a> seçilir.</li>
<li><b>Batarya:</b> Varsa batarya ayırıcısı açılıp kilitlenir.</li>
<li><b>Bekleme ve doğrulama:</b> İnverter kondansatörleri için üreticinin belirttiği süre beklenir; DC ve AC taraflarda gerilim, uygun kategoride ölçüm cihazıyla doğrulanır. Bkz. <a href="/post/dene-eked-test-adimi">Dene: test adımı</a>.</li>
<li><b>Kilit ve etiket:</b> Her çalışan kendi kilidini takar; çok noktalı izolasyonlarda anahtarlar <a href="/post/loto-kilit-kutusu-nasil-kullanilir">grup kilitleme kutusunda</a> toplanır. Tüm noktalara <a href="/eked-uyari-etiketleri">uyarı etiketi</a> asılır.</li>
<li><b>Devreye alma:</b> İş bitince herkes kendi kilidini çıkarır; önce DC, sonra AC taraf üretici sırasına göre devreye alınır.</li>
</ol>

<h2>Panel ve Kablo Üzerinde Çalışırken</h2>
<ul>
<li>Panel dizisinin kablolarında çalışılacaksa dizinin her iki ucu izole edilmeli; gerekiyorsa paneller ışık geçirmez bir örtüyle kapatılmalıdır.</li>
<li>Konnektörler yük altında çıkarılmamalı, çıkarılan uçlar yalıtılmalıdır.</li>
<li>Hasarlı panellerde gövdeye kaçak olabileceği unutulmamalıdır.</li>
</ul>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Yalnızca AC şalteri kapatıp DC tarafı enerjili bırakmak</li>
<li>DC ayırıcıyı inverter çalışırken yük altında açmak</li>
<li>İnverter kapandıktan hemen sonra kapağı açmak</li>
<li>Birden fazla inverterin aynı panoya bağlı olduğunu gözden kaçırmak (bkz. <a href="/post/jenerator-ve-ups-bakiminda-loto">çift beslemeli panolar</a>)</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-PE-E010S','LS-EK-S1100VV','LS-8812S']))}
<p>Şalter tiplerine göre doğru kilidi seçmek için <a href="/post/salter-kilidi-cesitleri">şalter kilidi çeşitleri</a> yazımıza, tüm modeller için <a href="/salter-kilitleme-ekipmanlari">şalter kilitleme ekipmanları</a> kategorimize bakabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

F2=[
 ('Asansör bakımında LOTO nasıl uygulanır?','Makine dairesindeki (veya makine dairesiz asansörlerde kontrol panelindeki) ana şalter kapatılıp kişisel kilitle kilitlenir, uyarı etiketi asılır ve asansörün çalışmadığı doğrulanır. Hidrolik asansörlerde ayrıca hidrolik basınç ve kabinin konumu kontrol edilmelidir.'),
 ('Asansör ana şalteri kilitlenebilir mi?','Asansör standartları, ana şalterin açık konumda kilitlenebilir olmasını öngörür. Bu kilitleme noktası, kişisel emniyet asma kilidiyle kullanılmalıdır; anahtar yalnızca kilidi takan kişide kalmalıdır.'),
 ('Ana şalter kapatılınca kabin aydınlatması da kesilir mi?','Genellikle hayır. Kabin aydınlatması ve bazı yardımcı devreler ana şalterden bağımsız beslenir. Bu devrelerde çalışılacaksa onların da ayrıca izole edilmesi gerekir.'),
 ('Kuyu dibi stop butonu veya revizyon modu LOTO yerine geçer mi?','Hayır. Kuyu dibi stop şalteri ve kabin üstü revizyon kumandası, bakım sırasında hareketi kontrol etmek için kullanılan emniyet düzenekleridir; enerji izolasyonu sağlamaz. Hareket gerektirmeyen işlerde ana şalter kilitlenmelidir.'),
 ('Asansör bakımında hangi ürünler gerekir?','Ana şalter için şalter kilitleme ekipmanı veya doğrudan emniyet asma kilidi, yardımcı devreler için minyatür şalter kilitleri, çoklayıcı, uyarı etiketleri ve kat kapılarında kullanılacak uyarı/bariyer ekipmanları gerekir.'),
]
B2=f'''
<p><b>Asansörler</b>; fabrikalar, iş merkezleri, hastaneler ve konutlarda en sık bakım gören ekipmanlardan biridir. Asansör bakımında kazaların büyük kısmı, kabinin veya karşı ağırlığın <b>beklenmedik hareketi</b> ile ilgilidir. Bu yazıda asansör bakımında LOTO uygulamasını ve sahada sık yapılan hataları anlatıyoruz.</p>

<h2>Asansörde Enerji Kaynakları</h2>
{table(['Enerji','Nerede?','Risk','Kontrol'],[
 ['Elektrik (ana besleme)','Makine dairesi ana şalteri / kontrol panosu','Kabinin hareket etmesi','<a href="/salter-kilitleme-ekipmanlari">Şalter kilidi</a> + kişisel kilit'],
 ['Elektrik (yardımcı devreler)','Kabin aydınlatması, priz, havalandırma','Elektrik çarpması','Ayrı izolasyon'],
 ['Yerçekimi','Kabin, karşı ağırlık','Fren açılırsa hareket, düşme','Kabini güvenli konuma alma, mekanik blokaj'],
 ['Hidrolik','Hidrolik asansör pistonu, ünite','Kabinin inmesi','Kabini tampona indirme, vana kilitleme'],
 ['Mekanik','Halat, kasnak, regülatör','Kapılma, sıkışma','Elektriksel izolasyon + hareketsizlik kontrolü'],
])}

<h2>Adım Adım Asansör LOTO</h2>
<ol>
<li><b>Bilgilendirme ve kapatma:</b> Bina sorumlusu bilgilendirilir; kat kapılarına “bakım var” uyarısı ve gerekirse bariyer konur.</li>
<li><b>Kabini konumlandırma:</b> Yapılacak işe göre kabin güvenli bir konuma (genellikle en alt kat veya makine dairesine erişim konumu) getirilir.</li>
<li><b>Ana şalter izolasyonu:</b> Ana şalter kapatılıp kişisel emniyet asma kilidiyle kilitlenir. Kilitleme yeri yoksa uygun <a href="/post/salter-kilidi-cesitleri">şalter kilidi</a> kullanılır.</li>
<li><b>Yardımcı devreler:</b> Kabin aydınlatması, kumanda veya priz devrelerinde çalışılacaksa bu devrelerin <a href="/post/minyatür-şalter-etiketleme-kilitleme-ürünleri">minyatür şalterleri</a> de kilitlenir.</li>
<li><b>Hidrolik asansörler:</b> Kabin tampona indirilir veya mekanik olarak desteklenir; ünite vanaları üretici talimatına göre kapatılıp kilitlenir. Bkz. <a href="/post/pnomatik-ve-hidrolik-sistemlerde-loto">hidrolik sistemlerde LOTO</a>.</li>
<li><b>Kilit ve etiket:</b> Birden fazla teknisyen varsa <a href="/coklandiricilar">çoklayıcı</a> kullanılır; her kilide <a href="/eked-uyari-etiketleri">uyarı etiketi</a> asılır.</li>
<li><b>Doğrulama:</b> Kat çağrısı ve kabin içi butonlarla hareket denenir; asansör hareket etmemelidir. Ardından enerjisizlik ölçüm cihazıyla kontrol edilir.</li>
<li><b>Devreye alma:</b> İş bitince alet ve malzemeler kuyudan alınır, herkes kendi kilidini çıkarır, asansör test sürüşleriyle hizmete alınır.</li>
</ol>

<h2>Revizyon Modu ve Stop Butonları</h2>
<p>Kabin üstü revizyon (bakım) kumandası ve kuyu dibi stop şalterleri, <b>hareket gerektiren</b> bakım işlerinde teknisyenin hareketi kontrol etmesini sağlar. Bunlar acil durdurma ve kontrol düzenekleridir; enerji izolasyonu değildir. Ayar ve test gibi enerji gerektiren işler dışında, kuyu veya kabin üstünde yapılacak tüm işler için ana şalter kilitlenmelidir. Benzer fark için bkz. <a href="/post/acil-stop-ve-emniyet-salteri-loto-farki">acil stop ile LOTO farkı</a>.</p>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Makine dairesi kapısını kilitleyip ana şalteri kilitlememek</li>
<li>Kabin aydınlatması ana şalterden beslenmiyor diye devrenin enerjisiz olduğunu sanmak</li>
<li>Hidrolik asansörde kabini desteklemeden piston veya hortum üzerinde çalışmak</li>
<li>Kat kapılarına uyarı koymamak</li>
<li>Asansör firmasının ve bina personelinin farklı kilitleme kurallarıyla çalışması (bkz. <a href="/post/taseron-yuklenici-firmalarda-loto-uygulamasi">taşeron firmalarda LOTO</a>)</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-X02C','LS-8773D','LS-8812S']))}
<p>Kişisel set içeriği için <a href="/post/kisisel-loto-seti-nedir-icinde-neler-olmali">kişisel LOTO seti</a> yazımıza, benzer uygulamalar için <a href="/post/gezer-vinc-bakiminda-loto">gezer vinç bakımında LOTO</a> yazımıza göz atabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

P=[
 dict(slug='gunes-enerjisi-santrallerinde-ges-loto', date='2026-10-30T09:10:00.000Z',
      title='Güneş Enerjisi Santrallerinde (GES) LOTO: DC Taraf, İnverter ve Pano Bakımında Kilitleme',
      seo_title='GES Bakımında LOTO: Güneş Enerjisi Santrali İş Güvenliği | Locksan Safety',
      desc='Güneş enerjisi santrallerinde (GES) LOTO (EKED) nasıl uygulanır? Kapatılamayan DC gerilim, inverter kondansatörleri, DC ayırıcı ve sigorta kilitleme, AC pano izolasyonu ve gerekli ürünler.',
      faq=F1, body=B1, cover_lines=['Güneş Enerjisi','Santrallerinde','(GES) LOTO'], letter='GES', lab='GÜNEŞ ENERJİSİ', step='Uygulama Rehberi'),
 dict(slug='asansor-bakiminda-loto', date='2026-10-30T09:00:00.000Z',
      title='Asansör Bakımında LOTO: Makine Dairesi, Kabin ve Kuyu Çalışmalarında Kilitleme',
      seo_title='Asansör Bakımında LOTO ve İş Güvenliği | Locksan Safety',
      desc='Asansör bakımında LOTO (EKED) nasıl uygulanır? Ana şalter kilitleme, yardımcı devreler, yerçekimi ve hidrolik asansör riskleri, revizyon modu ve stop butonlarının LOTO ile farkı, gerekli ürünler.',
      faq=F2, body=B2, cover_lines=['Asansör','Bakımında','LOTO'], letter='ASN', lab='ASANSÖR', step='Uygulama Rehberi'),
]
publish(P)
print('ok')
