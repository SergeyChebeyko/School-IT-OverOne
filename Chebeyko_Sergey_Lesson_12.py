#Дз (Chebeyko_Sergey_Lesson_12.py)
# 1. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
#2. В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов.
lines = ('Привет Мир.', 'Мама мыла раму.', 'Я люблю лето.')
with open('example.txt', 'w', encoding='utf-8') as f:
    for i in lines:
        f.write(i+'\n')
with open('example.txt', 'a', encoding='utf-8') as f:
    for i in lines:
        b = ''
        for j in i:
            if j.isalpha():
                b += j
        print(len(b))
        l = len(b)
        f.write(str(l)+'\n')
    print(len(lines))
    t = len(lines)
    f.write(str(t)+'\n')
# 3. Есть список состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.
S = ['5','яблоко','груша','1','4','лето','7']
alfa = []
digit = []
with open('example_2.txt', 'w', encoding='utf-8') as f:
    for i in S:
        if i.isalpha():
            alfa.append(i)
            alfa.sort(key=len)
        elif i.isdigit():
            digit.append(i)
            digit.sort()
    print(alfa)
    print(digit)
    f.write(str(alfa)+'\n')
    f.write(str(digit)+'\n')
# 4. Добавьте на свой РАБОЧИЙ СТОЛ папку my_name, в ней создайте 3 текстовых файла через цикл: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os
import os
print(os.getcwd())
os.mkdir('my_name') # Либо удаляем, либо комент.
os.chdir('my_name') # Меняет текущую директорию на указанную
print(os.getcwd())
for i in range(1,4):
    with open(f'test_{i}.txt', 'w') as f:
        print(f'test_{i}.txt')
os.rename('test_1.txt','rename_1.txt')
os.rename('test_2.txt','rename_2.txt')
os.rename('test_3.txt','rename_3.txt')
os.rmdir('my_name')