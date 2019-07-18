import random



bilgisayar=0
oyuncu=0
i=1

while (True):

    a = random.choice('tkm')
    print(a)

    b = input("bir karakter girin(t,k,m):")
    print(b)
    if a == b:
        bilgisayar += 1
        oyuncu += 1
        print("berabere")
        continue
    elif a == 't' and b == 'k':
        oyuncu += 1
        print("oyuncu kazandı")
        continue
    elif a == 't' and b == 'm':
        bilgisayar += 1
        print("bilgisayar kazandı")
        continue
    elif a == 'k' and b == 't':
        bilgisayar += 1
        print("bilgisayar kazandı")
        continue
    elif a == 'k' and b == 'm':
        oyuncu += 1
        print("oyuncu kazandı")
        continue
    elif a == 'm' and b == 't':
        oyuncu += 1
        print("oyuncu kazandı")
        continue
    elif a == 'm' and b == 'k':
        bilgisayar += 1
        print("oyuncu kazandı")
        continue
    i+=1
    if (i == 10):
         break


if oyuncu>bilgisayar:
    print("kazandınız")
elif oyuncu==bilgisayar:
    print("berabere")
else:
    print("kayebettiniz") 
