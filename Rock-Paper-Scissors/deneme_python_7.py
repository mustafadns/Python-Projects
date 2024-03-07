# ! Türkçe
# Taş - Kağıt - Makas Oyunu 

# ! English
# Rock - Paper - Scissors Game

from random import randint 


print(("-" * 30) + "\n Taş Kağıt Makas Oyunu \n" + ("-" * 30))

point = 0

while True:
    options = ["taş" , "kağıt" , "makas", "oyunu bitir"]
    computer = options[randint(0,2)]

    print(("-" * 50))
    options = input("1-taş \n2-kağıt \n3-makas \n4-oyunu bitir!!!\nSeçiminiz?: ")
    print(("-" * 50))

    if options == computer:
        print("SONUÇ: Berabere!!! (0 puan)")
    elif options == "taş":
        if computer == "kağıt":
            point = point - 1 
            print("SONUÇ: Kaybettiniz... (-1 puan)", computer, options,"'ı sarar.")
        else :
            point = point + 1 
            print("SONUÇ: Kazandınız... (+1 puan)", options, computer,"'ı kırar.")
    elif options == "kağıt":
        if computer == "makas":
            point = point - 1
            print("SONUÇ: Kaybettiniz... (-1 puan)", computer, options,"'ı keser.")
        else :
            point = point - 1
            print("SONUÇ: Kaybettiniz... (-1 puan)", computer, options,"'ı sarar.")
    elif options == "makas":
        if computer == "taş":
            point = point - 1
            print("SONUÇ: Kaybettiniz... (-1 puan)", computer, options,"'ı kırar.")
        else :
            point = point + 1
            print("SONUÇ: Kazandınız... (+1 puan)", options, computer,"'ı keser.")
    elif options == "oyunu bitir":
        print("Final puanınız:", point)
        break
    else :
        print("Bir seçenek giriniz ya da oyunu biritiniz")