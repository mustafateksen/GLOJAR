from gtts import gTTS
import os
import string
import time
"""
Unutma, eğer bütün seslendirmeler mp3 olarak hazır bulunursa uygulama çok
yer  kaplar. Bu sorunu atlatmak için önce google text-to-speech kullanarak dosyaları kaydetmeli,
sonra bunu playsound kütüphanesi ile oynatmalısın. Playsound, çünkü os kütüphanesindeki dahili
ses oynatma modülü arkaplanda değil, önplanda çalışıyor. Playsound'da ise tam tersi.
"""
uzanti=str("C:\ ")
uzantiglo=str("C:\GLOJAR")
uzantihafiza=str("C:\GLOJAR\hafiza.txt")
sayac=0
hafizadenetleme=os.path.isfile(uzantihafiza)
klasordenetleme=os.path.exists(uzantiglo)
if str(input("Kurulum işlemini yapmak ister misiniz?(E/H)   "))=="E" :
     if klasordenetleme==False:
          os.mkdir(uzantiglo)
          print("----------------------------------------------------------------------------------------------------------")
          print(uzanti + " Konumuna GLOJAR setup klasörü kuruldu.")
          print("----------------------------------------------------------------------------------------------------------")
          time.sleep(1.3)
     elif klasordenetleme==True:
          print("----------------------------------------------------------------------------------------------------------")
          print(uzanti +  " Konumunda GLOJAR setup klasörü BULUNDU!")
          print("----------------------------------------------------------------------------------------------------------")
          time.sleep(1.3)
     #Windows işletim sisteminde C:\ konumunda GLOJAR klasörünün bulunup bulunmadığına bakar.
     #Eğer yoksa yeni bir GLOJAR klasörü oluşturur.
     #(dosya kayıt için komut!) dosya.flush()
     if hafizadenetleme==False:
          hafiza= open(uzantihafiza,"a", encoding="utf-8")
          print("----------------------------------------------------------------------------------------------------------")
          print(uzantiglo +" Konumuna hafiza.txt adıyla ana hafıza kuruldu.")
          print("----------------------------------------------------------------------------------------------------------")
          time.sleep(1.3)
     elif hafizadenetleme==True:
          print("----------------------------------------------------------------------------------------------------------")
          print(uzantiglo +" Konumunda hafiza.txt BULUNDU!")
          print("----------------------------------------------------------------------------------------------------------")
          time.sleep(1.3)
while True:
     print("-------------------------------------------------------------------------------------------------------------")
     print("Glojarsetup.py terminali üzerinden yapmak istediğiniz başka dosya-klasör işlemi var ise")
     komut=str(input("birleşik ve hepsi küçük bir şekilde gerekli komut dizisini ekrana yazınız.      "))
     if komut=="yok" or komut=="uygulamayıkapat" or komut=="uygulamayıkapa":
          print("Komut dizisinden çıkılıyor, lütfen müdahale etmeyiniz.")
          time.sleep(1.5)
          while True:
               print("Kurulumu bitirme %"+  str(sayac))
               sayac=sayac+ 3
               time.sleep(0.08)
               if sayac>=100:
                    print("-------------------------------------------------------------------------------------------------------------")
                    print("KOMUT DİZİSİNDEN BAŞARIYLA ÇIKILDI!")
                    print("-------------------------------------------------------------------------------------------------------------")
                    print(" GLOJAR™ ' i kullandığınız için teşekkür eder, iyi günler dileriz.")
                    time.sleep(2)
                    break
          break
     elif komut=="hafızasil" or komut=="hafızayısil":
          os.remove(uzantihafiza)
          print("HAFIZA SİLİNİYOR. DOSYA BOYUTUNA GÖRE UZUN SÜREBİLİR.")
          while True:
               print("Hafıza Silme %"+  str(sayac))
               sayac=sayac+ 3
               time.sleep(0.08)
               if sayac>=100:
                    print("-------------------------------------------------------------------------------------------------------------")
                    print("Hafıza başarıyla siilindi.")
                    print("-------------------------------------------------------------------------------------------------------------")
                    print(" GLOJAR™ ' i kullandığınız için teşekkür eder, iyi günler dileriz.")
                    time.sleep(2)
                    break
          break
     elif komut=="sil" or komut=="herşeyisil" or komut=="herseyisil" or komut=="klasörüsil" or komut=="klasörsil" or komut=="klasorsil" or komut=="klasorusil":
          os.remove(uzantihafiza)
          os.rmdir(uzantiglo)
          print("HAFIZA VE BÜTÜN VERİLER SİLİNİYOR. DOSYA BOYUTUNA GÖRE UZUN SÜREBİLİR.")
          while True:
               print("Veri silme %"+  str(sayac))
               sayac=sayac+ 3
               time.sleep(0.08)
               if sayac>=100:
                    print("-------------------------------------------------------------------------------------------------------------")
                    print("Uygulama önbelleğindeki ve kayıt edilmiş tüm veriler başarıyla silindi.")
                    print("-------------------------------------------------------------------------------------------------------------")
                    print(" GLOJAR™ ' i kullandığınız için teşekkür eder, iyi günler dileriz.")
                    time.sleep(2)
                    break
          break
     else:
          print("BİLİNMEYEN TERMİNAL KODU! HATA ALINMAMAK İÇİN UYGULAMA KAPATILIYOR.")
          
          
