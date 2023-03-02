# #1
a = input("Введите пароль - ")
b = input("Введите пароль повторно - ")
if a==b:
    print("пароль принят")
else:
    print("пароль не принят")
# #2
a = int(input("Введите номер вагона - "))
if a <= 50:
    if a % 2 == 0:
        print ("плацкарт - верхнее")
    else:
        print ("плацкарт - нижнее")
elif a > 50 and a % 2 == 0:
    print ("купе - верхнее")
else:
    print("купе - нижнее")
# #3
year = int(input("Введите год - "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("год", year, "високосный")
else:
    print("год", year, "невисокосный")
# #4
c1= str(input("цвет 1"))
c2= str(input("цвет 2"))
c = ('красный','синий','желтый')
if c1 in c and c2 in c:
    if c1 != c2:
        if (c1 in ('красный','синий')) and (c2 in ('красный','синий')):
            print('фиолетовый')
        if (c1 in ('красный','желтый')) and (c2 in ('красный','желтый')):
            print('оранжевый')
        if (c1 in ('синий','желтый')) and (c2 in ('синий','желтый')):
            print('зеленый')
    else: print(c1)
else:
    print("ошибка цвета")
#5
n = int(input("введите n - "))
i = 0
m = list()
while i < n:
    m.append(input("добавьте слово"))
    i = i + 1
print(str(m))
