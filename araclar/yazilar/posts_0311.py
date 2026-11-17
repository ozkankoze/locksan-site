import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from addpost import *

F1=[
 ('Silo ve bunker bakımında neden LOTO gerekir?','Silolarda helezon (vidalı konveyör), döner valf, sürgülü kapak ve karıştırıcı gibi hareketli ekipmanlar ile depolanmış malzemenin ağırlığı bulunur. Bakım veya temizlik sırasında bu ekipmanların çalışması ya da malzemenin akması ezilme, kapılma ve gömülme kazalarına yol açabilir. Tüm enerji kaynakları izole edilip kilitlenmelidir.'),
 ('Siloya girmek için LOTO yeterli mi?','Hayır. Silo içi çalışma aynı zamanda kapalı alan çalışmasıdır. LOTO’ya ek olarak çalışma izni, ortam ölçümü (oksijen, gaz, toz), havalandırma, emniyet kemeri ve gözcü gibi kapalı alan önlemleri uygulanmalıdır.'),
 ('Pnömatik sürgülü kapak nasıl kilitlenir?','Kapağın hava beslemesi vana ile kesilip kilitlenir, silindirdeki basınç tahliye edilir. Kapak kapalı konumda mekanik olarak da sabitlenmelidir; aksi halde malzeme ağırlığıyla veya kalan hava ile hareket edebilir.'),
 ('Malzeme köprülenmesi (kemerlenme) neden tehlikelidir?','Silo duvarlarında asılı kalan veya köprü oluşturan malzeme aniden çökebilir. Bu nedenle tıkanıklık açma işleri mümkün olduğunca silonun dışından, uygun ekipmanla yapılmalı; içeri girilmeden önce alt boşaltma ekipmanları kilitlenmelidir.'),
 ('Silo bakımında hangi LOTO ürünleri gerekir?','Motor ve pano şalterleri için şalter kilitleri, pnömatik hatlar için vana ve pnömatik bağlantı kilitleri, çok kişili işler için grup kilitleme kutusu ve çoklayıcı, emniyet asma kilitleri ve uyarı etiketleri gerekir.'),
]
B1=f'''
<p>Çimento, un, yem, plastik granül, kimya ve gıda tesislerinde <b>silo ve bunkerler</b> sürekli temizlik ve bakım gerektirir. Bu işler, ekipman kazaları ile kapalı alan risklerinin bir arada bulunduğu en tehlikeli işler arasındadır. Silonun altındaki bir helezonun çalışması ya da kapalı sanılan bir sürgünün açılması, içerideki çalışan için ölümcül olabilir. Bu yazıda silo ve bunker bakımında LOTO uygulamasını özetliyoruz.</p>

<h2>Silolarda Enerji Kaynakları ve Riskler</h2>
{table(['Enerji / risk','Nerede?','Sonuç','Kontrol'],[
 ['Elektrik','Helezon, döner valf, karıştırıcı, vibratör motorları','Kapılma, ezilme','<a href="/salter-kilitleme-ekipmanlari">Şalter kilidi</a> + kişisel kilit'],
 ['Pnömatik','Sürgülü kapak, hava şoklayıcı (air blaster), akışkanlaştırıcı','Ani hareket, basınçlı hava','<a href="/pnomatik-baglanti-kilitleme-ekipmanlari">Pnömatik kilit</a> + tahliye'],
 ['Yerçekimi / malzeme','Silo içindeki ürün, köprülenmiş malzeme','Gömülme, çökme','Boşaltma ekipmanlarını kilitleme, dışarıdan müdahale'],
 ['Besleme','Silo dolum hattı, elevatör, pnömatik taşıma','Çalışırken malzeme gelmesi','Dolum hattını izole etme'],
 ['Kapalı alan','Silo içi atmosfer, toz','Boğulma, toz patlaması','Çalışma izni, ölçüm, havalandırma'],
])}

<h2>Adım Adım Silo LOTO</h2>
<ol>
<li><b>Çalışma izni:</b> İş için yazılı çalışma izni düzenlenir; kapalı alan giriş gerekiyorsa kapalı alan önlemleri planlanır. Bkz. <a href="/calisma-izni-ve-kilitleme-proseduru">çalışma izni ve kilitleme prosedürü</a>.</li>
<li><b>Boşaltma ve durdurma:</b> Silo mümkün olduğunca boşaltılır; dolum ve boşaltma ekipmanları normal şekilde durdurulur.</li>
<li><b>Dolum hattını izole etme:</b> Siloyu besleyen elevatör, konveyör veya pnömatik taşıma hattı durdurulup kilitlenir. Bkz. <a href="/post/konveyor-bakiminda-loto-nasil-uygulanir">konveyör bakımında LOTO</a>.</li>
<li><b>Boşaltma ekipmanlarını kilitleme:</b> Helezon, döner valf ve karıştırıcıların motor şalterleri kapatılıp kilitlenir. Bkz. <a href="/post/motor-koruma-salteri-kilitleme">motor koruma şalteri kilitleme</a>.</li>
<li><b>Pnömatik sistemler:</b> Sürgülü kapak, hava şoklayıcı ve akışkanlaştırıcıların hava beslemesi kapatılıp kilitlenir, basınç tahliye edilir. Sürgü kapalı konumda mekanik olarak sabitlenir. Bkz. <a href="/post/pnomatik-ve-hidrolik-sistemlerde-loto">pnömatik sistemlerde LOTO</a>.</li>
<li><b>Grup kilitleme:</b> Çok noktalı izolasyonlarda izolasyon kilitlerinin anahtarları <a href="/post/loto-kilit-kutusu-nasil-kullanilir">grup kilitleme kutusuna</a> konur; siloya girecek her çalışan kendi kişisel kilidini kutuya takar.</li>
<li><b>Doğrulama:</b> Her ekipman yerel ve uzak kumandadan çalıştırılmayı denenerek kontrol edilir. Bkz. <a href="/post/dene-eked-test-adimi">Dene: test adımı</a>.</li>
<li><b>Devreye alma:</b> İş bitince silo içi kontrol edilir, herkes çıktıktan sonra kilitler sahipleri tarafından çıkarılır ve ekipmanlar kontrollü şekilde devreye alınır.</li>
</ol>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Sadece boşaltma helezonunu kilitleyip dolum hattını unutmak</li>
<li>Pnömatik sürgünün hava beslemesini kesip basıncı tahliye etmemek</li>
<li>Hava şoklayıcıların ayrı bir hava tankından beslendiğini gözden kaçırmak</li>
<li>Kapalı alan ölçümü yapmadan siloya girmek</li>
<li>Köprülenmiş malzemenin altında veya üzerinde çalışmak</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-8812S','LS-PS02S','LS-X07UN']))}
<p>Sektöre özel uygulamalar için <a href="/post/gida-sektorunde-loto-eked">gıda sektöründe LOTO</a> ve <a href="/post/kimya-ve-petrokimya-tesislerinde-loto">kimya tesislerinde LOTO</a> yazılarımıza göz atabilirsiniz. Tesisinizdeki izolasyon noktalarını belirlemek için <a href="/saha-arastirmasi">saha araştırması</a> hizmetimizden yararlanabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

F2=[
 ('Atık su arıtma tesisinde LOTO neden önemlidir?','Arıtma tesislerinde pompalar, karıştırıcılar, blowerlar ve çamur sıyırıcılar seviye şalterleri veya SCADA ile otomatik çalışır. Ayrıca hatlarda su basıncı ve havuzlarda kapalı alan riskleri bulunur. Bakım sırasında ekipmanın beklenmedik çalışmasını önlemek için enerji kaynakları kilitlenmelidir.'),
 ('Dalgıç pompa bakımında nelere dikkat edilmeli?','Pompanın beslemesi panodan kapatılıp kilitlenmeli, seviye şamandırası veya SCADA ile otomatik çalışma engellenmeli, basma hattı vanası kapatılıp kilitlenmeli ve hat basıncı tahliye edilmelidir. Pompa kuyudan çıkarılırken kaldırma ekipmanı ve askı güvenliği de kontrol edilmelidir.'),
 ('Çekvalf olması geri akışı önlemek için yeterli mi?','Hayır. Çekvalfler sızdırabilir veya arızalanabilir. Bakım yapılan pompanın basma hattındaki izolasyon vanası kapatılıp kilitlenmeli, ara bölüm tahliye edilmelidir.'),
 ('Havuz veya kuyu içinde çalışırken LOTO yeterli mi?','Hayır. Islak kuyu, havuz ve kanallar kapalı alan olarak değerlendirilir; hidrojen sülfür (H₂S) gibi gazlar oluşabilir. LOTO’ya ek olarak çalışma izni, gaz ölçümü, havalandırma ve kurtarma planı gerekir.'),
 ('Arıtma tesisinde hangi LOTO ürünleri kullanılır?','Pompa ve motor panoları için şalter kilitleri, sürgülü ve kelebek vanalar için vana kilitleri, ulaşılması zor noktalarda kablolu kilitler, emniyet asma kilitleri, çoklayıcılar ve suya dayanıklı uyarı etiketleri kullanılır.'),
]
B2=f'''
<p>Belediye ve sanayi tesislerinin <b>atık su arıtma tesisleri</b>; dalgıç pompalar, karıştırıcılar, havalandırma blowerları, çamur sıyırıcı köprüler, dekantörler ve çok sayıda vanadan oluşur. Bu ekipmanların büyük kısmı <b>seviye şalterleri veya SCADA ile otomatik çalışır</b>. Bakım ekibinin bilmeden “bekleyen” bir pompanın kendiliğinden çalışması, arıtma tesislerinde sık görülen bir risktir.</p>

<h2>Arıtma Tesisinde Enerji Kaynakları</h2>
{table(['Ekipman','Enerji','Risk','Kontrol'],[
 ['Dalgıç ve kuru pompalar','Elektrik, hat basıncı','Otomatik çalışma, basınçlı su','<a href="/salter-kilitleme-ekipmanlari">Şalter kilidi</a> + vana kilidi'],
 ['Karıştırıcı ve havalandırıcılar','Elektrik, mekanik','Kapılma','Motor şalterini kilitleme'],
 ['Blowerlar','Elektrik, basınçlı hava','Ani çalışma, basınç','Şalter + hava hattı vanası kilitleme'],
 ['Çamur sıyırıcı köprüler','Elektrik, mekanik','Ezilme, sıkışma','Ana şalter kilitleme'],
 ['Vanalar ve hatlar','Hidrostatik basınç','Geri akış, su basması','<a href="/vana-kilitleme-ekipmanlari">Vana kilitleme</a> + tahliye'],
 ['Kuyu ve havuzlar','Kapalı alan atmosferi (H₂S)','Zehirlenme, boğulma','Çalışma izni, gaz ölçümü'],
])}

<h2>Adım Adım Pompa ve Ekipman LOTO</h2>
<ol>
<li><b>Planlama:</b> Bakım yapılacak ekipman, SCADA ve kontrol odası ile birlikte belirlenir; otomatik çalışma senaryoları (seviye, zamanlayıcı, yedek pompa devreye girmesi) gözden geçirilir.</li>
<li><b>Durdurma:</b> Ekipman normal şekilde durdurulur; SCADA’da “bakımda” durumuna alınır.</li>
<li><b>Elektrik izolasyonu:</b> Motor beslemesi panodan kapatılıp kilitlenir. Pompa ve karıştırıcılarda genellikle <a href="/post/motor-koruma-salteri-kilitleme">motor koruma şalteri</a> veya <a href="/post/kompakt-şalter-etiketleme-kilitleme-ürünleri">kompakt şalter</a> kilitlenir.</li>
<li><b>Hidrolik izolasyon:</b> Pompanın emme ve basma vanaları kapatılıp kilitlenir. Arıtma tesislerinde yaygın olan <a href="/post/sürgü-simit-vana-etiketleme-kilitleme-ürünleri">sürgülü (şiber) vanalar</a> ve <a href="/post/kelebek-vana-kilitleme-ekipmanlari">kelebek vanalar</a> için uygun kilitler seçilir. Ara bölüm tahliye edilir. Bkz. <a href="/post/cekvalf-kilitleme-loto">çekvalf ve LOTO</a>.</li>
<li><b>Kilit ve etiket:</b> Her çalışan kendi kilidini takar; çok noktalı işlerde <a href="/post/loto-kilit-kutusu-nasil-kullanilir">grup kilitleme kutusu</a> kullanılır. Nemli ortamlara dayanıklı <a href="/eked-uyari-etiketleri">uyarı etiketleri</a> tercih edilir.</li>
<li><b>Doğrulama:</b> Yerel kumanda ve SCADA üzerinden çalıştırma denenir; ekipman çalışmamalıdır.</li>
<li><b>Devreye alma:</b> İş bitince alan kontrol edilir, herkes kendi kilidini çıkarır, vanalar kontrollü açılır ve ekipman otomasyona geri alınır.</li>
</ol>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Pompayı SCADA’dan durdurup panoyu kilitlememek</li>
<li>Yedek pompanın otomatik devreye girebileceğini unutmak</li>
<li>Çekvalfe güvenip basma hattı vanasını kilitlememek</li>
<li>Uzak ve dağınık vanalarda kilit yerine sadece etiket kullanmak</li>
<li>Islak kuyuya gaz ölçümü yapmadan girmek</li>
</ul>

<h2>Önerilen Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-VN-02','LS-8812S','LS-X07UN']))}
<p>Vana tiplerine göre kilit seçimi için <a href="/post/vana-valf-kilitleme-rehberi">vana ve valf kilitleme rehberimize</a>, dağınık izolasyon noktaları için <a href="/post/kablo-kilidi-nedir-cesitleri">kablo kilidi</a> yazımıza bakabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

P=[
 dict(slug='silo-ve-bunker-bakiminda-loto', date='2026-11-03T09:10:00.000Z',
      title='Silo ve Bunker Bakımında LOTO: Helezon, Sürgü ve Kapalı Alan Riskleri',
      seo_title='Silo ve Bunker Bakımında LOTO ve İş Güvenliği | Locksan Safety',
      desc='Silo ve bunker bakımında LOTO (EKED) nasıl uygulanır? Helezon, döner valf, pnömatik sürgülü kapak, hava şoklayıcı ve malzeme köprülenmesi riskleri; adım adım kilitleme ve gerekli ürünler.',
      faq=F1, body=B1, cover_lines=['Silo ve Bunker','Bakımında','LOTO'], letter='SİLO', lab='SİLO / BUNKER', step='Uygulama Rehberi'),
 dict(slug='atik-su-aritma-tesislerinde-loto', date='2026-11-03T09:00:00.000Z',
      title='Atık Su Arıtma Tesislerinde LOTO: Pompa, Karıştırıcı ve Vana Kilitleme',
      seo_title='Atık Su Arıtma Tesislerinde LOTO: Pompa ve Vana Kilitleme | Locksan Safety',
      desc='Atık su arıtma tesislerinde LOTO (EKED) nasıl uygulanır? Dalgıç pompa, karıştırıcı, blower ve çamur sıyırıcı kilitleme, SCADA ile otomatik çalışma, çekvalf ve kapalı alan riskleri, gerekli ürünler.',
      faq=F2, body=B2, cover_lines=['Atık Su Arıtma','Tesislerinde','LOTO'], letter='SU', lab='ARITMA TESİSİ', step='Uygulama Rehberi'),
]
publish(P)
print('ok')
