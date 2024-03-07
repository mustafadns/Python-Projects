# ! Türkçe
#belirtilen sayıya kadar olan asal sayıları sıralama

# ! English
#sorting prime numbers up to the specified number

print(("-" * 30) + "\n Kaça Kadar Asal Sayı İstiyorsun \n" + ("-" * 30))


List = []

def prime_number(number):
    if number == 1:
        print("1 sayısını giremezsiniz!!!")
    for numbers in range(2 , number + 1):
        if numbers > 1:
            for i in range(2 , numbers):
                if (numbers % i) == 0:
                    break
            else:
                List.append(numbers)
    return List

number = int(input("Sayı Giriniz:"))
print("Cevap: {}".format(prime_number (number)))