"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem: ax^2 + bx + c

Deltayı (Diskriminantı) Hesaplama: b^2 - 4ac

Birinci Kök: (-b - delta^1/2) / (2a)
İkinci Kök: (-b + delta^1/2) / (2a)

Not: Delta eğer 0'dan büyükse 2 reel kök vardır. Eğer 0'a eşit ise 1 reel kök vardır. Eğer 0'dan küçük ise reel kök yoktur denebilir.
"""

print("2. Dereceden Bir Denklemin Köklerini Bulan Programa Hoşgeldiniz\nDenklemin oluşabilmesi için ax^2 + bx + c formülündeki; a, b, c değelerini giriniz.")



a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("Denklem: {}x^2 + {}x + {}\n".format(a,b,c))

delta = b ** 2 - 4 * a * c
print("Verdiğiniz değerlere göre hesaplanan delta: ",delta)

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

if(delta<0):
    print("Girdiğiniz değerlerdeki denklemin deltası 0 dan küçük olduğu için denklemin reel kökü bulunmamaktadır. Ancak sizin için karmaşık köklerini bulabiliriz.\nBirinci kök: {}\nİkinci kök: {}".format(x1,x2))

elif(delta==0):
    print("Girdiğiniz değerlerdeki denklemin deltası 0 olduğu için denklemin tek bir reel kökü vardır.\nDenklemin kökü: ",x1)

else:
    print("Girdiğiniz değerlerdeki denklemin kökleri aşağıdadır.\nBirinci Kök: {}\nİkinci Kök: {}".format(x1,x2))






