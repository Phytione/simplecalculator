sayi1=int(input("İlk sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
print("***************")
print("1-Toplama İşlemi")
print("2-Çıkarma İşlemi")
print("3-Çarpma İşlemi")
print("4-Bölme İşlemi")
islem=input("Yapmak istediğiniz işlemi seçiniz....")

if islem=="1":
    print("Sonuc:",sayi1+sayi2)
    
elif islem=="2":
    print("Sonuc:",sayi1-sayi2)

elif islem=="3":
    print("Sonuc:",sayi1*sayi2)

elif islem=="4":
    print("Sonuc:",sayi1/sayi2)

else:
    print("Lütfen geçerli bir değer giriniz...")
      

      
    
  
    


