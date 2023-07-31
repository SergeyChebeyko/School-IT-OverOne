# ДЗ на четверг (Файл называем Chebeyko_Sergey_Lesson_2.py):
# Ознакомиться с модулями random и math и их командами
# Вычислить сумму цифр случайного трёхзначного числа с помощью операторов % и //
# Само число создаем через модуль random

from random import random

n = random() * 900 + 100

n = int(n)

print(n)

a = n // 100

b = (n // 10) % 10

c = n % 10

print(a+b+c)





