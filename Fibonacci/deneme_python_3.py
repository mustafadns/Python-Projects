# ! Türkçe 
#uzunluğa göre fibonacci dizisi sıralama 

# ! English
#sorting the fibonacci sequence by length


print(("-" * 30) + "\n Ne Kadar Fibonacci Dizisi Olsun \n" + ("-" * 30))

def fibonacci(n, output=[]):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
        output.append(str(a))
    return output

number = int(input("\nİstediğiniz fibonacci dizisi sayısını giriniz: "))

print("Cevap: {}".format(",".join(fibonacci(number))))