# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 22:22:29 2025

@author: Hasret Sultan
"""
"""
VERİ BİLİMİİ YAZ KAMPI 2.HAFTA ÖDEVİ 
"""
 # SORU1: Kullanıcıdan bir sayı isteyin.
 #Sayı pozitif, negatif ya da sıfır mı kontrol edin.
 #Aynı zamanda tek/çift olup olmadığını da belirtin.
 #Çıktı örneği: "Pozitif Çift" veya "Negatif Tek" gibi.
 
sayi = int(input("Bir sayı giriniz: "))
if sayi == 0:
    print("Sıfır, Çift Sayı")
else:
    durum = "Pozitif" if sayi > 0 else "Negatif"
    tek_cift = "Çift" if sayi % 2 == 0 else "Tek"
    print(f"{durum} {tek_cift} Sayı ")

#Soru 2 Kullanıcıdan bir kelime alın.
# Hangi harften kaç tane geçtiğini bulun.
# Sonucu dictionary olarak gösterin.
#Örnek: "data" → {'d': 1, 'a': 2, 't': 1}
kelime= input("Bir kelime giriniz:").lower()
my_dict= {}
for harf in kelime:
    if harf not in my_dict:
      my_dict[harf] = 1
    else:
      my_dict[harf] += 1
    
print (my_dict)
   
#Soru 3 Kullanıcıdan şifre girmesini isteyin. Şifre:
# En az 8 karakter olmalı
# En az 1 büyük harf içermeli
# En az 1 rakam içermeli
#Koşulları sağlayıp sağlamadığına göre kullanıcıyı bilgilendirin.
 
sifre=input("Lütfen Şifrenizi Oluşturun:")
uzunluk = len(sifre) >= 8
buyuk_harf = any(harf.isupper() for harf in sifre)
rakam = any(harf.isdigit() for harf in sifre)

if uzunluk and buyuk_harf and rakam:
    print("Şifre geçerli ")
else:
    print("Şifre geçersiz ")
    if not uzunluk:
        print("- En az 8 karakter olmalı")
    if not buyuk_harf:
        print("- En az 1 büyük harf içermeli")
    if not rakam:
        print("- En az 1 rakam içermeli")
        
#Soru4 [12, 4, 9, 25, 30, 7, 18] listesini kullanın. 
#Listenin ortalamasını bulun 
#Ortalamadan büyük sayıları ayrı bir listeye atın. 
#Sonucu ekrana yazdırın.

toplam=0
liste1=[12,4,9,25,30,7,18]
for i in liste1:
    toplam+=i
ort=toplam/7
liste2=[]
for i in liste1:
    if i >ort:
        liste2.append(i)
print(liste2)

#soru5 üçgen desen oluşturma sorusu
for i in range (1,6):
     print("*" * i)

#Soru6 Kullanıcıdan sürekli sayı isteyin. 
#Kullanıcı 0 girdiğinde program dursun. 
# Girilen tüm sayıların toplamını ve ortalamasını yazdırın.
sayilar=[]
while sayi!=0 :
    sayi=int(input("Bir sayı giriniz:"))
    sayilar.append(sayi)
toplamı=0   
for i in sayilar :
    toplamı+=i
ortalaması=toplamı/len(sayilar)
print (f"Girilen sayıların toplamı :{toplamı} , ortalaması :{ortalaması}")

#Soru7 Kullanıcıdan bir kelime isteyin. 
# Kelimenin palindrom olup olmadığını kontrol edin. 

kelime=input("Bir kelime giriniz:")
tersi=kelime[::-1]
if kelime == tersi :
    print (kelime,"kelimesi palindrom.")
else :
    print(kelime,"kelimesi palindrom değil .")
    
#Soru8 1’den 100’e kadar olan sayılardan: 
# Hem 3’e hem 5’e bölünebilenlerin karelerini içeren bir liste oluşturun. 
# Sonucu ekrana yazdırın.

my_list=[]
for x in range (1,101):
    if x%15==0:
        my_list.append(x**2)
print (my_list)  

#Soru9 Bir cümle alın. 
# Cümledeki kelimeleri split() ile ayırın. 
# Her kelimenin ilk harfini büyük yaparak yeni bir string oluşturun. 
# Örnek: "python veri bilimi" → "Python Veri Bilimi"     

cumle=input ("Lütfen bir cümle giriniz:")
kelimeler=cumle.split()
yeni_kelimeler = []
for kelime in kelimeler:
    yeni_kelimeler.append(kelime.lower().capitalize()) 
    
yeni_cumle = " ".join(yeni_kelimeler)
print(yeni_cumle)

#Soru 10 Mini Proje – Film Yorumu Analizi
yorumlar_list=[]
yorum=None
while yorum!="*":
    yorum=input ("Çıkmak için * a basınız ya da yorum yazınız :")
    if yorum!="*":
        yorumlar_list.append(yorum)
    else:
        print("Yorum bölümü kapandı")
toplam_uzunluk=0
iyi_sayacı=0   
for y in yorumlar_list:
     toplam_uzunluk+=len(y)
     if "iyi" in y :  
        iyi_sayacı+=1
yorum_sayısı=len(yorumlar_list)
ortalama_uzunluk=toplam_uzunluk/yorum_sayısı
en_uzun = max(yorumlar_list, key=len)
en_kisa = min(yorumlar_list, key=len)

print(f"Toplam yorum sayısı :{yorum_sayısı} ")
print(f"İyi geçen yorum sayısı:{iyi_sayacı}")
print(f"En uzun yorum :{en_uzun}")
print(f"En kısa yorum:{en_kisa}")
print (f"Ortalama uzunluk:{ortalama_uzunluk}")





        
     


    









