# NVDA için bilgisayar klavyesiyle braille giriş desteği #

* Yazarlar: NV Access Limited, Noelia Ruiz Martínez
* Telif hakkı: 2012-2019 NV Access Limited, Noelia Ruiz Martínez
* Lisans: GNU General Public lisansı sürüm 2.0
* [kararlı sürümü][1] indir: (NVDA 2019.3 ve üzeri sürümlerle uyumludur)
* [geliştirici sürümünü][2] indir: (NVDA 2019.3 ve üzeri sürümlerle
  uyumludur)
* [Sürüm 2014.1][3] (NVDA 2017.3-2019.2 sürümleriyle uyumludur)

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

## Nasıl ayarlanır?

NVDA menüsü tercihler alt menüsünde bulunan NVDA ayarları iletişim
kutusundaki NVDA için bilgisayar klavyesinden braille giriş desteği
kategorisinden eklentiyi ayarlayabilirsiniz. Eklentinin ayarlar iletişim
kutusunu açmak için girdi hareketleri iletişim kutusunun konfigürasyon
kategorisinden kısayol tuşu da atayabilirsiniz.

Tek elle yazmak istiyorsanız ilgili onay kutusunu işaretleyin. İki elle
yazmak istiyorsanız onay kutusunu işaretsiz bırakın.

Tek elle yazarken NVDA'nın noktaları söylemesini de sağlayabilirsiniz.

## Nasıl kullanılır?

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

		* 1, 2, 3, 4, 5, 6, 7 ve 8. noktalar için sol el tuşları f, d, s, r, e, w,
		  a ve q'dur. 
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

Bazı klavyeler, özellikle dizüstü bilgisayar klavyeleri bazı tuş
kombinasyonlarını desteklemez. Basılan tuşlar Windows veya NVDA tarafından
algılanmadığı için bu sorun çözülemez. Bastığınız tuşların bir üst
sırasındaki tuşlara basmayı deneyebilirsiniz. 

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

[1]: https://addons.nvda-project.org/files/get.php?file=pckbbrl

[2]: https://addons.nvda-project.org/files/get.php?file=pckbbrl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pckbbrl-o

