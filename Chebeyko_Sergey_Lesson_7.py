print("\033[1m\033[43m\033[42m""Домашнее задание №7, Чебейко Сергей Леонидович""\033[0m")

print('В списке, содержащем положительные и отрицательные целые числа,'
      'вычислите сумму чётных положительных элементов.')

a = [1, 2, 3, -5, -4, -2, 4]
s = 0
for i in range(len(a)):
    if a[i] % 2 == 0 and a[i] > 0:
        s += a[i]
print(s)

def mylist():
    mlist=[i for i in range(-10,10) if i >0 and (i%2==0)]
    print(mlist)
    return mlist
if __name__ == '__main__':
    mylist()

print('Найти в списке те элементы, значение которых меньше среднего арифметического,'
      'взятого от всех элементов списка.')

print('Вариант 1')
lst = [5, 3, 2, 5, 6, 2, 1, 4, 5]
lst_sum = sum(lst)
lst_len = len(lst)
lst_avg = lst_sum/lst_len
new_lst = []
for i in lst:
    if i < lst_avg:
        new_lst.append(i)
print(new_lst)


print('Вариант 2')
from random import random
n = 10
o = [0] * n
for i in range(n):
    o[i] = int(random() * 10)
print(o)
t = sum(o)/n
print("средне арифметическое", t)
less = []
for i in range(n):
    if o[i] < t:
        less.append(o[i])
print(less)