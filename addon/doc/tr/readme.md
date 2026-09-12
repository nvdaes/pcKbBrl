# NVDA için bilgisayar klavyesiyle braille giriş desteği #

* Yazar: NV Access Limited, Noelia Ruiz Martínez
* Telif Hakkı: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* Lisans: GNU General Public lisansı sürüm 2.0

Bu eklenti bilgisayar klavyesiyle braille yazabilmenizi sağlar. Şimdilik
aşağıdaki klavye düzenleri desteklenmektedir:

* İngilizce QWERTY klavye.
* Fransızca (Fransa).
* Almanca (Almanya).
* İtalyanca (İtalya).
* Farsça.
* Portekizce (Portekiz).
* İspanyolca (İspanya ve Meksika).
* Türkçe.

## Nasıl yapılandırılır

NVDA menüsü tercihler alt menüsünde bulunan NVDA ayarları iletişim
kutusundaki NVDA için bilgisayar klavyesinden braille giriş desteği
kategorisinden eklentiyi ayarlayabilirsiniz. Eklentinin ayarlar iletişim
kutusunu açmak için girdi hareketleri iletişim kutusunun konfigürasyon
kategorisinden kısayol tuşu da atayabilirsiniz.

Tek elle yazmak istiyorsanız ilgili onay kutusunu işaretleyin. İki elle
yazmak istiyorsanız onay kutusunu işaretsiz bırakın.

Tek elle yazarken NVDA'nın noktaları söylemesini de sağlayabilirsiniz.

Tek elle yazarken noktaların otomatik olarak gönderilmesini istiyorsanız,
0'dan büyük bir zaman aşımı ayarlamak için döndürme kontrolünü kullanın.

Ayrıca, tek elle yazarken nokta göndermek, temizlemek ve oluşturmak için
karakterlerin yanı sıra tek elde veya standart modda yok sayılacak
karakterleri de ayarlayabilirsiniz.

Eklenti ayarları panelinde varsayılanları geri yüklemek de mümkündür.

## Nasıl kullanılır

1. Braille girişi etkinleştirmek için NVDA+0 kısayol tuşunu
   kullanın. Kısayolu girdi hareketleri iletişim kutusunun braille
   kategorisinden değiştirebilirsiniz.
2. Braille klavyede yazıyormuş gibi bilgisayar klavyesindeki tuşlara aynı
   anda basın.

	* İki elle yazmak istiyorsanız aşağıdaki tuşları kullanın. Tuşlar Türkçe
	  QWERTY klavyeye göre belirtilmiştir. Başka bir klavye düzeni
	  kullanıyorsanız belirtilen tuşlara denk gelen tuşları kullanın:

		* 1, 2 ve 3. noktalar için f, d ve s.
		* 4, 5 ve 6. noktalar için j, k ve l.
		* 7 ve 8. noktalar için a ve ş tuşlarını kullanın.
		* Bir üst sıradaki tuşları da kullanabilirsiniz. Yani q, w, e, r, u, ı, o
		  ve p.

	* Tek elle yazmak isterseniz tuşlara aynı anda veya teker teker
	  basabilirsiniz. İstediğiniz harfi yazdığınızda g veya h'ye
	  basın. Yazarken yanlış nokta kullanırsanız t veya y tuşuna basarak harfi
	  yeniden yazabilirsiniz. Türkçe QWERTY klavyede kullanılan tuşlar
	  aşağıdadır:

		* Sol el: 1, 2, 3, 4, 5, 6, 7 ve 8 noktaları için f, d, s, r, e, w, a, q.
		* Sağ elle yazmak için j, k, l, u, ı, o, ş ve p tuşlarını
		  kullanabilirsiniz.

3. Boşluk, back space, enter ve f tuşları gibi diğer çoğu tuş normal
   işlevini gerçekleştirir. Alt+shift tuşlarına birlikte basmamaya dikkat
   edin. Klavye düzeni değişeceğinden girilen noktalar değişebilir.
4. Braille ekran kullanıyormuş gibi sistem imlecini hareket ettirmek veya
   üzerinde bulunduğunuz satırı okutmak için boşluk tuşuyla birlikte braille
   noktalara basın. Örneğin Boşluk+1. nokta yukarı ok, boşluk+4, 5 ve
   6. noktalar ctrl+end tuşu işlevini görür. Boşluk+1 ve 4. noktalar
   üzerinde bulunduğunuz satırı okur.
5. Braille girişini devredışı bırakmak için NVDA+0 kısayol tuşunu kullanın.

## Önemli notlar

Eklenti NVDA'nın braille girişi desteğini kullanır. NVDA'nın braille
ayarları iletişim kutusunda seçilen braille tablosu kullanılır.

Bazı klavyeler, özellikle de dizüstü bilgisayar klavyeleri, basılan belirli
tuş kombinasyonlarını kaldıramaz.  Bu durumda, belirli tuşlar basitçe yok
sayılır.  Ne yazık ki, tuşlar Windows veya NVDA tarafından hiçbir zaman
alınmadığı için bunu düzeltmek için yapılabilecek bir şey yoktur.  Bazı
durumlarda, klavyeniz bu tuşlara izin verebileceğinden, üst sıradaki tuşları
bir veya iki elinizle kullanmak yardımcı olabilir.

## 44.0.0 için değişiklikler

* Kannada.cti tablosu eklendi.

## 28.0.0 için değişiklikler

* Tek el modu için varsayılan değerler değiştirildi.

## 2023.02.23 için değişiklikler

* Noktaları tek el modunda yazmak için kullanılan tuşları yapılandırma
  özelliği eklendi.
* Artık braille ile yazarken göz ardı edilmesi gereken tuşları
  yapılandırabilirsiniz.
* Eklenti ayarları paneline varsayılanlara geri yükle düğmesi eklendi.
* NVDA 2023.1 ile uyumlu.

## 2022.1 için değişiklikler

* Tek elle yazarken noktaları göndermek ve silmek için tuşları yapılandırma
  yeteneği eklendi. Ayrıca, onay tuşlarına basmadan noktaların otomatik
  olarak gönderilmesi için bir zaman aşımı süresi ayarlamak da mümkündür.

## 2021.1 için değişiklikler

* NVDA, Tek el modu etkin olmadığında veya boşluğa basıldığında noktaları
  söylemeye çalışmaz.
* NVDA 2021.1 ile uyumlu.

## 2020.1 sürümü için değişiklikler

* Braille ekranlardaki komutlara benzer olarak boşluk tuşuyla birlikte
  braille noktalara basarak bazı komutları uygulayabilirsiniz.
* Tek el modunda tek noktaları söyleme seçeneği eklendi.

## Katkıda bulunanlar

* James Teh
* Noelia.
* Mohammadreza Rashad
* Çağrı Doğan
* Bernd Dorer
* Ângelo Abrantes
* Cyrille Bougot
* Abdel.

[[!tag dev stable]]

