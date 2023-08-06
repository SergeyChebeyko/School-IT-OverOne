import random

print("\033[1m\033[43m\033[42m""Домашнее задание №11, Чебейко Сергей Леонидович""\033[0m")


print('1.Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.')
import random

Maxtrix = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        Maxtrix[i][j] = random.randint(-20,20)
        print(Maxtrix[i][j], end='\t')
    print()

my_sum =0

for i in Maxtrix:
    if sum(i) > my_sum: my_sum=sum(i)
print(my_sum)

print('2. Найти максимальный элемент диагонали матрицы.')

Maxtrix = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        Maxtrix[i][j] = random.randint(-20,20)
        print(Maxtrix[i][j], end='\t')
    print()
max_el = 0
for i in range(5):
    if Maxtrix[i][i]>max_el: max_el = Maxtrix[i][i]
print(max_el)

print('3. Вычислить количество отрицательных элементов под главной диагональю матрицы.')

Maxtrix = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        Maxtrix[i][j] = random.randint(-20,20)
        print(Maxtrix[i][j], end='\t')
    print()
count = 0
for i in range(5):
    for j in range(5):
        if Maxtrix[i][j]<0 and j<i: count += 1
print(count)

print('4. Найти сумму каждой строки')

from random import random
M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random()*11))
        print("%3d" % b[j], end='')
    a.append(b)
    print('   |', sum(b))

for i in range(M):
    print(" ", end='')
print()

print("Задача 2 Задача Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое\n "
"на второе. Обработать ошибку деления на ноль. Если второе число 0, то программа запрашивает ввод чисел заново.\n"
"Также если были введены буквы,то обработать исключение. Придумать и обработать исключения на\n "
"TypeError и ValueError, IndexError")

while True:
    try:
        number_1 = int(input('Введите число: '))
        number_2 = int(input('Введите число: '))
        c = number_1/number_2
    except ValueError:
        pass
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    else:
        print(c)
        break