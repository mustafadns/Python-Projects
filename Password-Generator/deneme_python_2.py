# ! Türkçe
#verilen uzunluk ve levele göre şifre oluşturucu

# ! English
#password generator according to the given length and level

import random
import string

def generate_password(length, level, output=[]):
    chars = string.ascii_letters
    if level > 1:
        chars = "{}{}".format(chars, string.digits)
    if level > 2:
        chars = "{}{}".format(chars, string.punctuation)
    
    for i in range(length):
        output.append(random.choice(chars))
    
    return "".join(output)

print(("-" * 30) + "\n Şifre Belirleyici\n" + ("-" * 30))

password_length = int(input("Şifre Uzunluk: "))
print("\n 0:en basit \n 1:orta \n 2-...:güçlü")
password_level = int(input("Şifre Seviye:"))

password = generate_password(password_length, password_level)
print("\nSizin için en güvenilir şifre: {}".format(password))