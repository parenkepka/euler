# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

x = 0
y = 0
a = 0
b = 0
c = 0
d = 0

#считаем сумму чисел кратную 3
while True:
    if x < 1000:
        y += x
        x += 3
    elif x >= 1000:
        break 

#считаем сумму чисел кратную 5
while True:
    if a < 1000:
        b += a
        a += 5
    elif a >= 1000:
        break 

#считаем сумму чисел кратную 15, чтобы потом вычесть из общей суммы для исключения повторов по 3 и 5
while True:
    if c < 1000:
        d += c
        c += 15
    elif c >= 1000:
        break 

summ = b + y - d
print(summ)