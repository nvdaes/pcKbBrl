# NVDA İçin PC Klavyesinden Braille Girişi

* Yazarlar: NV Access Limited, Noelia Ruiz Martínez
* Telif hakkı: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* Lisans: GNU Genel Kamu Lisansı sürüm 2.0

Bu NVDA eklentisi, bilgisayar klavyesi aracılığıyla Braille olarak metin girilmesine olanak tanır.
Şu anda aşağıdaki klavye düzenleri desteklenmektedir:

* İngilizce QWERTY klavye.
* Fransızca (Fransa).
* Almanca (Almanya).
* İtalyanca (İtalya).
* Farsça.
* Portekizce (Portekiz).
* İspanyolca (İspanya ve Meksika).
* Türkçe.

## Nasıl yapılandırılır

Eklenti, NVDA menüsünün “Tercihler” alt menüsü altında yer alan Ayarlar iletişim kutusundaki ilgili kategoriden yapılandırılabilir. Eklenti ayarları panelini açmaya yarayan bir hareket, “Girdi hareketleri” iletişim kutusundaki “Yapılandırma” kategorisinden atanabilir.

Tek elle yazmak istiyorsanız ilgili onay kutusunu işaretleyin veya standart kipte (iki elle) yazmayı tercih ediyorsanız işaretli olmadığından emin olun.

Ayrıca, "tek el modu" özelliğini kullanarak NVDA'nın tek bir nokta yazıp yazmayacağını da seçebilirsiniz.

Tek elle yazarken noktaların otomatik olarak gönderilmesini istiyorsanız, zaman aşımını 0'dan büyük bir değere ayarlamak için döndürme kontrolünü kullanın.

Ayrıca, tek elle yazarken gönderilecek, silinecek ve oluşturulacak noktaları belirleyebileceğiniz gibi, tek elle veya standart kipte göz ardı edilecek karakterleri de ayarlayabilirsiniz.

Eklenti ayarları panelinden varsayılan ayarlara geri dönmek de mümkündür.

## Nasıl Kullanılır

1. Braille girişini etkinleştirmek için NVDA+0 tuşlarına basın. Bu hareket, Girdi hareketleri iletişim kutusundaki Braille kategorisinden değiştirilebilir.
2. PC klavyesindeki tuşlara, sanki bir braille klavyesiymiş gibi aynı anda basarak braille yazın.
	* İki elinizi kullanarak metin girmek istiyorsanız, QWERTY İngilizce klavye kullanıyorsanız aşağıdaki tuşları, diğer klavye düzenlerinde ise ilgili konumlardaki tuşları kullanın:
		* 1, 2 ve 3 numaralı noktalar için sırasıyla f, d ve s harfleri kullanılmıştır.
		* 4, 5 ve 6 numaralı noktalar için sırasıyla j, k ve l harfleri kullanılmıştır.
		* 7 ve 8 numaralı noktalar için sırasıyla a ve ş tuşlarını kullanın.
		* Yukarıdaki satırdaki tuşları da kullanabilirsiniz; yani q, w, e, r, u, ı, o ve p.
	* Tek elle metin yazmak istiyorsanız, tuşlara aynı anda veya birkaç tuş vuruşuyla basarak, istediğiniz karaktere karşılık gelen noktaları ekleyerek karakterleri oluşturabilirsiniz. Tüm noktaları ekledikten sonra karakteri yazmak için g veya h tuşuna basın. Bir karakter oluştururken hata yaparsanız, yazmadan önce t veya y tuşuna basarak noktaları silebilirsiniz. QWERTY İngilizce klavyede kullanılan tuşlar şunlardır:
		* Sol el: 1, 2, 3, 4, 5, 6, 7 ve 8 noktaları için f, d, s, r, e, w, a, q.
		* Sağ el: j, k, l, u, ı, o, ş, p (1, 2, 3, 4, 5, 6, 7 ve 8 numaralı noktalar için).
3. Aralık tuşu, geri tuşu, enter tuşu ve fonksiyon tuşları dahil olmak üzere diğer tuşların çoğuna normal şekilde basabilirsiniz. Alt+Shift tuşlarına basmamaya dikkat edin, çünkü klavye düzenini değiştirmek girilen noktaları etkileyebilir.
4. Sistemin imlecini hareket ettirmek (veya geçerli satırı bildirmek) için, tıpkı bir braille ekranı kullanıyormuşsunuz gibi, aralık tuşuna braille noktalarıyla birlikte basın. Örneğin, yukarı ok tuşunu taklit etmek için aralık+nokta 1, control+end tuşlarını taklit etmek için aralık+nokta 4+nokta 5+nokta 6, geçerli satırı bildirmek için aralık+nokta 1+nokta 4 vb.
5. Braille girişini devre dışı bırakmak için NVDA+0 tuşlarına basın.

## Önemli Notlar

Bu eklenti, NVDA'nın yerleşik Braille giriş desteğini kullanır.
Bu nedenle, kullanılan girdi tablosu, NVDA'nın Braille Ayarları iletişim kutusunda belirtilen tablodur.

Bazı klavyeler, özellikle dizüstü bilgisayar klavyeleri, belirli tuş kombinasyonlarına basılmasını desteklemez.
Bu durumda, bazı tuşlar basitçe göz ardı edilir.
Ne yazık ki, bu sorunu gidermek için yapılabilecek hiçbir şey yoktur; zira tuşlara basıldığında Windows ya da NVDA tarafından hiçbir zaman algılanmamaktadır.
Bazı durumlarda, klavyeniz bu tuşlara izin veriyorsa, üst sıradaki tuşları tek elle veya iki elle kullanmak yardımcı olabilir.

## 44.0.0 için değişiklikler

* Kannada.cti tablosu eklendi.

## 28.0.0 için değişiklikler

* Tek el modu için varsayılan değerler değiştirildi.

## 2023.02.23 Tarihine Ait Değişiklikler

* Tek elle nokta yazma modunda kullanılan tuşları yapılandırma özelliği eklendi.
* Artık Braille alfabesiyle yazarken göz ardı edilmesi gereken tuşları yapılandırabilirsiniz.
* Eklenti ayarları paneline "Varsayılan ayarlara geri yükle" düğmesi eklendi.
* NVDA 2023.1 ile uyumlu.

## 2022.1 için Değişiklikler

* Tek elle yazarken nokta gönderme ve silme tuşlarını yapılandırma özelliği eklendi. Ayrıca, onay tuşlarına basmadan noktaları otomatik olarak göndermek için bir zaman aşımı ayarlamak da mümkün.

## 2021.1 için Değişiklikler

* NVDA, tek el kipi etkin değilken veya boşluk tuşuna basıldığında noktaları seslendirmeye çalışmaz.
* NVDA 2021.1 ile uyumlu.

## 2020.1 için Değişiklikler

* Braille ekranlarında bulunan komutlara benzer şekilde, hareketleri taklit etmek için aralık tuşuna braille noktalarıyla birlikte basabilirsiniz.
* Tek elle yazılan noktalara sesli komut ekleme seçeneği eklendi.

## Katkıda Bulunanlar

* James Teh
* Noelia.
* Mohammadreza Rashad
* Çağrı Doğan
* Bernd Dorer
* Ângelo Abrantes
* Cyrille Bougot
* Abdel.
