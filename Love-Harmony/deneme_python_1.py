# ! Türkçe 
#Çiftlerin isimlerine göre aşk uyumluluklarını ölçen uygulama

# ! English
#The application that measures the compatibility of love according to the names of couples


print(("-" * 30) + "\n Ne Kadar Uyumlusunuz \n" + ("-" * 30))

name1 = input("Sizin isminiz:")
name2 = input("Sevgilinizin ismi:")

love = len(name1) + len(name2)

if len(name1) > len(name2):
    love -= 5
else:
    love += 3

love *= 42
love = love / (100 + len(name2))

love = 10 if love > 10 else round(love , 0)

print ("{} ve {} çiftinin aşk oranı 10 üzerinden {} puandır.".format(name1,name2,love))
