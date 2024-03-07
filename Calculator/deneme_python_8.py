# ! Türkçe 
# Hesap makinesi yapımı 
# daha sonra kodlar daha dinamik hale getirilmek üzere düzenleme yapılacaktır 

# ! English
# Making a calculator
# then the codes will be edited to make them more dynamic

print(("-" * 30) + "\n Hesap Makinesi \n" + ("-" * 30))

# Toplama işlemi
def toplama(x, y):
    return x + y

# Çıkarma işlemi
def cikarma(x, y):
    return x - y

# Çarpma işlemi
def carpma(x, y):
    return x * y

# Bölme işlemi
def bolme(x, y):
    return x / y

print("Yapmak istediğiniz işlemi seçin:")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

secim = input("Seçiminiz (1/2/3/4):")

sayi1 = float(input("İlk sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    print(sayi1, "+", sayi2, "=", toplama(sayi1, sayi2))
elif secim == '2':
    print(sayi1, "-", sayi2, "=", cikarma(sayi1, sayi2))
elif secim == '3':
    print(sayi1, "*", sayi2, "=", carpma(sayi1, sayi2))
elif secim == '4':
    print(sayi1, "/", sayi2, "=", bolme(sayi1, sayi2))
else:
    print("Geçersiz giriş")