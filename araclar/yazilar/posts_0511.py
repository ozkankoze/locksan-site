import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from addpost import *

F1=[
 ('Forklift bakımında LOTO nasıl uygulanır?','Forklift durdurulup çatal yere indirilir, park freni çekilir, kontak anahtarı alınır. Elektrikli forkliftlerde akü bağlantısı ayrılır ve fiş kilitleme ekipmanıyla kilitlenir; dizel ve LPG forkliftlerde anahtar kişisel kilitle muhafaza altına alınır. Araca “bakımda, kullanmayın” etiketi asılır.'),
 ('Kontak anahtarını almak yeterli mi?','Tek başına yeterli değildir; yedek anahtarlar olabilir ve elektrikli araçlarda akü enerjisi devrede kalır. Anahtar kişisel kilitle bir kutuda veya torbada kilitlenmeli, elektrikli araçlarda akü fişi de kilitlenmelidir.'),
 ('Akü fişi nasıl kilitlenir?','Akü konnektörü ayrıldıktan sonra uç, fiş kilitleme ekipmanının içine yerleştirilip emniyet asma kilidiyle kilitlenir. Böylece akü yeniden bağlanamaz.'),
 ('Çatal ve direkte nelere dikkat edilmeli?','Hidrolik sistem basınç altında olabilir; çatal ve direk yerçekimiyle inebilir. Çatal altında çalışılacaksa mekanik destek veya emniyet zinciri kullanılmalı, hidrolik basınç üretici talimatına göre tahliye edilmelidir.'),
 ('Akü şarj istasyonunda LOTO gerekir mi?','Şarj cihazı veya şarj hattı üzerinde bakım yapılacaksa evet; şarj cihazının beslemesi panodan kapatılıp kilitlenmelidir. Ayrıca akü şarj alanında hidrojen gazı ve asit riskine karşı önlem alınmalıdır.'),
]
B1=f'''
<p>Depo, lojistik ve üretim tesislerinin en yoğun kullanılan araçları <b>forkliftler, transpaletler ve istif makineleridir</b>. Bu araçların bakım ve onarımı sırasında başka bir çalışanın aracı fark etmeden çalıştırması veya kaldırılmış çatalın aşağı inmesi ciddi kazalara yol açabilir. Mobil ekipmanlarda LOTO, sabit makinelerden biraz farklı uygulanır. Bu yazıda forklift ve iş makinelerinde LOTO’yu anlatıyoruz.</p>

<h2>Forkliftte Enerji Kaynakları</h2>
{table(['Enerji','Nerede?','Risk','Kontrol'],[
 ['Elektrik (akü)','Çekiş ve kaldırma motorları, kontrol ünitesi','Aracın hareket etmesi, ark','Akü fişini ayırma + <a href="/pnomatik-baglanti-kilitleme-ekipmanlari">fiş kilidi</a>'],
 ['Yakıt / motor','Dizel ve LPG forkliftler','Motorun çalıştırılması','Kontak anahtarını kilit altına alma, LPG tüp vanasını kapatma'],
 ['Hidrolik','Direk, çatal, yana kaydırma silindirleri','Çatalın inmesi, ani hareket','Çatalı indirme, basınç tahliyesi'],
 ['Yerçekimi','Kaldırılmış çatal ve yük','Ezilme','Yükü indirme, mekanik destek'],
 ['Mekanik','Tekerlekler, şanzıman','Aracın kayması','Park freni, takoz'],
])}

<h2>Adım Adım Forklift LOTO</h2>
<ol>
<li><b>Güvenli park:</b> Araç düz zemine park edilir, çatal tamamen yere indirilir, park freni çekilir; gerekiyorsa tekerleklere takoz konur.</li>
<li><b>Kontak anahtarı:</b> Anahtar alınır ve bakım yapan kişinin kontrolünde, kişisel kilitle bir kutuda veya <a href="/ls-d71/fis-kilitleme-cantasi">kilitleme torbasında</a> muhafaza edilir.</li>
<li><b>Akü izolasyonu (elektrikli araç):</b> Akü konnektörü ayrılır ve <a href="/post/fis-kilidi-elektrik-ve-pnomatik-fis-kilitleme">fiş kilitleme ekipmanıyla</a> kilitlenir. Akü ayırıcı şalteri varsa o da kilitlenir.</li>
<li><b>Yakıt izolasyonu (LPG / dizel):</b> LPG tüp vanası kapatılır; gerekiyorsa vana kilitlenir.</li>
<li><b>Hidrolik ve yerçekimi:</b> Çatal yerdeyken hidrolik basınç üretici talimatına göre tahliye edilir. Kaldırılmış direk altında çalışılacaksa mekanik destek kullanılır. Bkz. <a href="/post/pnomatik-ve-hidrolik-sistemlerde-loto">hidrolik sistemlerde LOTO</a>.</li>
<li><b>Etiket:</b> Araca ve direksiyona görünür bir <a href="/eked-uyari-etiketleri">“bakımda, kullanmayın” etiketi</a> asılır.</li>
<li><b>Doğrulama:</b> Araç çalıştırılmayı ve hareket ettirilmeyi denenir; çalışmamalıdır.</li>
<li><b>Hizmete alma:</b> Bakım bitince kilitler sahibi tarafından çıkarılır, akü bağlanır, araç fren, direk ve korna testlerinden sonra hizmete alınır.</li>
</ol>

<h2>Diğer Mobil Ekipmanlar</h2>
<ul>
<li><b>Transpalet ve istif makineleri:</b> Akü fişi ayrılıp kilitlenir, anahtar alınır.</li>
<li><b>Makaslı platform ve personel yükselticiler:</b> Platform indirilir, ana akü şalteri kilitlenir.</li>
<li><b>İş makineleri (yükleyici, ekskavatör):</b> Kova ve kepçe yere indirilir, akü ayırıcı şalteri ve kontak anahtarı kilitlenir.</li>
</ul>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Anahtarı aracın üzerinde veya masada bırakmak</li>
<li>Elektrikli forkliftte akü fişini ayırmadan elektrik arızasına müdahale etmek</li>
<li>Kaldırılmış çatalın altında desteksiz çalışmak</li>
<li>Aracı etiketsiz bırakıp başka vardiyanın kullanmasına izin vermek</li>
</ul>

<h2>Önerilen Ürünler ve Setler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-X02C','LS-8773D','LS-PS02S']))}
<p>Fiş kilitleme ürünleri için <a href="/pnomatik-baglanti-kilitleme-ekipmanlari">pnömatik ve fiş kilitleme ekipmanları</a> kategorimize, kişisel set seçimi için <a href="/post/kisisel-loto-seti-nedir-icinde-neler-olmali">kişisel LOTO seti</a> yazımıza bakabilirsiniz. Ürünleri <a href="/teklif-sepeti">teklif sepetine</a> ekleyerek fiyat isteyebilirsiniz. Tüm ürünler {PIL} sayfamızda.</p>
'''

F2=[
 ('Vardiya değişiminde LOTO nasıl devredilir?','Bakım işi bir vardiyada bitmiyorsa, gelen vardiyanın çalışanı kendi kişisel kilidini izolasyon noktasına veya grup kilitleme kutusuna takar; ancak bundan sonra giden vardiyanın çalışanı kendi kilidini çıkarır. Böylece izolasyon hiçbir an korumasız kalmaz.'),
 ('Giden çalışan kilidini gelen çalışana verebilir mi?','Hayır. Kişisel kilit ve anahtarı devredilmez. Her çalışan kendi kilidini kullanır; devir, kilitlerin sırayla takılıp çıkarılmasıyla yapılır.'),
 ('Vardiya devrinde hangi bilgiler aktarılmalı?','Hangi enerji kaynaklarının izole edildiği, izolasyon noktalarının yeri, yapılan doğrulama, işin durumu, kalan riskler ve varsa geçici olarak verilen enerji (test) bilgisi yazılı olarak aktarılmalıdır.'),
 ('Grup kilitleme kutusu devirde ne işe yarar?','Çok noktalı izolasyonlarda izolasyon kilitleri yerinde kalır, anahtarları kutudadır. Devir sırasında sadece kutu üzerindeki kişisel kilitler değişir; izolasyon noktalarına dokunulmaz. Bu, devri hem hızlı hem güvenli yapar.'),
 ('Gece vardiyasında kilidini unutup giden olursa ne yapılır?','Bu durum yazılı istisna prosedürüyle yönetilir: kişiye ulaşılmaya çalışılır, ekipman ve alanın güvenli olduğu doğrulanır, yetkili onayıyla kilit kaldırılır ve kişi işe döndüğünde bilgilendirilir.'),
]
B2=f'''
<p>Büyük bakım işleri, revizyonlar ve arıza onarımları çoğu zaman tek vardiyada bitmez. <b>Vardiya değişimi</b>, LOTO’nun en sık zayıfladığı andır: Giden ekip kilitlerini çıkarır, gelen ekip henüz kilidini takmamıştır ve ekipman birkaç dakika korumasız kalır. Bu kısa boşluk ciddi kazalara yol açabilir. Bu yazıda vardiya değişiminde LOTO devrinin nasıl yapılacağını anlatıyoruz.</p>

<h2>Temel Kural: Önce Tak, Sonra Çıkar</h2>
<p>Devirde izolasyon <b>hiçbir an</b> korumasız kalmamalıdır. Bunun için sıra her zaman şöyledir:</p>
<ol>
<li>Gelen vardiyanın çalışanı <b>kendi kişisel kilidini</b> takar.</li>
<li>Ancak bundan sonra giden vardiyanın çalışanı <b>kendi kilidini</b> çıkarır.</li>
</ol>
<p>Kişisel kilitler ve anahtarlar <b>asla devredilmez</b>; her çalışan kendi kilidini kullanır. Bkz. <a href="/post/emniyet-kilidi-anahtar-sistemleri-kd-ka-mk">anahtar sistemleri</a>.</p>

<h2>Grup Kilitleme ile Devir</h2>
{table(['Adım','Giden vardiya','Gelen vardiya'],[
 ['1','İş durumunu ve izolasyon listesini hazırlar','Devir toplantısına katılır'],
 ['2','İzolasyon noktalarını birlikte gezer','Noktaları ve kilitleri kontrol eder'],
 ['3','—','Kendi kişisel kilidini grup kutusuna takar'],
 ['4','Kendi kişisel kilidini kutudan çıkarır','—'],
 ['5','Devir formunu imzalar','Devir formunu imzalar'],
])}
<p>İzolasyon kilitleri yerinde kalır; anahtarları <a href="/post/loto-kilit-kutusu-nasil-kullanilir">grup kilitleme kutusundadır</a>. Devirde sadece kutu üzerindeki kişisel kilitler değişir. Bu yöntem özellikle çok noktalı işlerde devri hızlı ve güvenli yapar. Uygun kutular için <a href="/grup-kilitleme-kutulari-ve-eked-cantalari">grup kilitleme kutuları</a> kategorimize bakabilirsiniz.</p>

<h2>Devir Formunda Bulunması Gerekenler</h2>
<ul>
<li>Ekipman ve iş tanımı</li>
<li>İzole edilen enerji kaynakları ve izolasyon noktalarının listesi</li>
<li>Kullanılan kilit ve etiket numaraları</li>
<li>Yapılan doğrulama (deneme / ölçüm) bilgisi</li>
<li>İşin mevcut durumu ve kalan riskler</li>
<li>Giden ve gelen sorumluların adı, imzası, tarih ve saat</li>
</ul>

<h2>Devirde Dikkat Edilecekler</h2>
<ol>
<li><b>Yüz yüze devir:</b> Devir mümkünse sahada ve yüz yüze yapılır; sadece telefonla veya not bırakarak yapılmaz.</li>
<li><b>Yeniden doğrulama:</b> Gelen ekip, işe başlamadan önce enerjisizliği kendisi de doğrular. Bkz. <a href="/post/dene-eked-test-adimi">Dene: test adımı</a>.</li>
<li><b>Geçici enerji verme:</b> Test için enerji verilecekse bu, devir formunda ayrıca belirtilir ve test sonrası izolasyon yeniden yapılır.</li>
<li><b>Taşeron ekipler:</b> Dış firmalar da aynı kurala uyar (bkz. <a href="/post/taseron-yuklenici-firmalarda-loto-uygulamasi">taşeron firmalarda LOTO</a>).</li>
<li><b>Unutulan kilit:</b> Sahibi ayrılmış bir kilit için yazılı istisna prosedürü uygulanır; kilit rastgele kesilmez.</li>
</ol>

<h2>Sık Yapılan Hatalar</h2>
<ul>
<li>Giden ekibin, gelen ekip gelmeden kilitlerini çıkarması</li>
<li>Kişisel kilidin veya anahtarın gelen çalışana verilmesi</li>
<li>Devrin sadece sözlü yapılması</li>
<li>Gelen ekibin enerjisizliği yeniden doğrulamaması</li>
</ul>

<h2>Önerilen Ürünler</h2>
{table(['Kod','Set','İçerik'],set_rows(['LS-8812S','LS-B1100S','LS-X02C']))}
<p>Prosedür hazırlığı için <a href="/post/loto-proseduru-ornegi">LOTO prosedürü örneği</a> ve <a href="/post/loto-denetim-kontrol-listesi">LOTO denetim kontrol listesi</a> yazılarımıza göz atabilirsiniz. Ekibinize özel eğitim için <a href="/egitim-ve-danismanlik">eğitim ve danışmanlık</a> sayfamızı ziyaret edin. Tüm ürünler {PIL} sayfamızda.</p>
'''

P=[
 dict(slug='vardiya-degisiminde-loto-devri', date='2026-11-05T09:10:00.000Z',
      title='Vardiya Değişiminde LOTO Devri: Kilitler Nasıl Güvenle Devredilir?',
      seo_title='Vardiya Değişiminde LOTO Devri Nasıl Yapılır? | Locksan Safety',
      desc='Bakım işi vardiyada bitmezse LOTO (EKED) nasıl devredilir? “Önce tak, sonra çıkar” kuralı, grup kilitleme kutusuyla devir, devir formu, yeniden doğrulama ve sık yapılan hatalar.',
      faq=F2, body=B2, cover_lines=['Vardiya','Değişiminde','LOTO Devri'], letter='24S', lab='VARDİYA DEVRİ', step='Prosedür Rehberi'),
 dict(slug='forklift-ve-is-makinelerinde-loto', date='2026-11-05T09:00:00.000Z',
      title='Forklift ve İş Makinelerinde LOTO: Akü, Anahtar ve Hidrolik Kilitleme',
      seo_title='Forklift Bakımında LOTO: Akü Fişi ve Anahtar Kilitleme | Locksan Safety',
      desc='Forklift, transpalet ve iş makinesi bakımında LOTO (EKED) nasıl uygulanır? Kontak anahtarı muhafazası, akü fişi kilitleme, LPG vanası, çatal ve hidrolik riskleri; adımlar ve ürünler.',
      faq=F1, body=B1, cover_lines=['Forklift ve İş','Makinelerinde','LOTO'], letter='FORK', lab='FORKLİFT', step='Uygulama Rehberi'),
]
publish(P)
print('ok')
