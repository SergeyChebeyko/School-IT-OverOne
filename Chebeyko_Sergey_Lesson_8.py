print("\033[1m\033[43m\033[42m""Домашнее задание №8, Чебейко Сергей Леонидович""\033[0m")

print('Задание №1 ♣Найти самое длинное слово в строке.♣')

txt = 'Это строка является демонстрацией. Пожалуйста, игнорируйте её!'
txt_list=txt.split()
len_list=[]
dict={}
for i in txt_list :
    len_list.append(len(i))
for l, t in zip (len_list ,txt_list ):
    dict[l] = t.replace(".", " ")
print(dict[max(len_list) ])


print('Задание №2 ♣Преобразовать текст в кортеж слов с удалением знаков препинания и других небуквенных знаков.♣')

import string

s = ['Это строка является демонстрацией. Пожалуйста, игнорируйте её!']
print(tuple(s))
tab = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
s = "Это строка является демонстрацией. Пожалуйста, игнорируйте её!"
s = s.translate(tab).split()
print(tuple(s))

print('----- \033[31mКак бы было правильно\033[0m<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('1 ЗАДАНИЕ')
a = 'Это строка является демонстрацией. Пожалуйста, игнорируйте её!'
for i in a:
    if i.isalpha()==False:
        a = a.replace(i, ' ')
print(a)
my_list = a.split() # также можно  my_list = a.split(' ')
print(my_list)
print(max(my_list, key=len))
print('2 ЗАДАНИЕ')
a = 'Это строка является демонстрацией. Пожалуйста, игнорируйте её!'
for i in a:
    if i.isalpha()==False:
        a = a.replace(i, ' ')
print(a)
my_list = a.split() # также можно  my_list = a.split(' ')
print(tuple(my_list))