# ! Türkçe
# girilen sayıya göre faktoriyel hesaplama 

# ! English
# factorial calculation according to the entered number

print(("-" * 30) + "\n Faktoriel Hesaplama \n" + ("-" * 30))

def factorial(number, fact=1):
    for i in range(1, number + 1):
        fact *= i
    return fact

number = int(input("Sayı giriniz:"))

print("Girdiğiniz sayının faktorieli: {}" .format(factorial(number)))
