print  ("Домашнее задание №3, Чебейко Сергей Леонидович")

print ("Задача №1: Определить, является ли год високосным")

years = int (input ("Пожалуйста, введите год запроса:"))

if years % 4 == 0 and years % 100 != 0:
         print ("годы, обычный високосный год")
elif years % 400 == 0:
         print ("годы, високосный год")
else:
         print ("«Не високосный год»")

print ("Задача №2: Определить существование треугольника и его тип")
#
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")

print ("Задача №3: Определить принадлежность точки кругу с центром в начале координат.")

from math import sqrt

x = float(input("x="))
y = float(input("y="))
r = float(input("r="))
h = sqrt(x**2 + y**2)
print("Расстояние до точки от начала координат равно %.2f" % h)
if h > r:
    print("точка находится за пределами круга")
else:
    print("точка принадлежит кругу")

print ("Задача №4: Творческое задание Придумать свою задачу на тему "
       "занятия. Обязательно использовать несколько вложений if-else(elif)")

a = int(input("Введите число: "))
if a < 5:
    print("Маленькое")
elif -5 <= a <= 5:
    print("Среднее")
else:
    print("Большое")