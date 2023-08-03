print ("\033[4m\033[35m\033[40m""Домашнее задание №5, Чебейко Сергей Леонидович""\033[0m")

print ("\033[3m\033[31m""1. Перемножить все нечётные значения в диапазоне от 1 до 100.""\033[0m")
a = 1
for x in range(1, 100, 2): a *= x
print(a)

print ("\033[3m\033[31m""2. Есть пустой список. Записать в этот список все числа в диапазоне "
       "от 1 до 500 кратные 5. Вывести на печать этот список.""\033[0m")
print("\033[1m\033[35m\033[40m""Вариант: 1""\033[0m")
a=1
b=500

for i in range(1,500):
    if i % 5 == 0:
        print(i, end= '|')


print(i, end= '\n')
print("\033[1m\033[35m\033[40m""Вариант: 2""\033[0m")
lower = int(input("Введите начальную границу диапазона:"))
upper = int(input("Введите окончательную границу диапазона:"))
n = int(input("Введите кратную:"))
for i in range(lower, upper + 1):
    if(i % n == 0):
        print(i, end = ',')
print(i, end = '\n')
print ("\033[3m\033[31m""3. Вывести на экран все чётные значения в диапазоне "
      "от 1 до 497, разделяя их запятой.""\033[0m")
a = ""
for n in range (1, 497):
    if 0 == n % 2:
        a += str(n) + ', '
        print(a)

print ("\033[3m\033[31m""4. Дан список чисел (задаете сами). Если число встречается более двух раз, то добавить его в новый список. "
       "Если число уже есть в новом списке, то не добавляем его.""\033[0m")

list_numbers = [1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 7]

def get_new_numbers(numbers):
    list_of_new_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_new_numbers.append(number)

    return list_of_new_numbers
print(get_new_numbers(list_numbers))

print("\033[3m\033[31m"'5. Дополнительная задача. Оформить таблицу умножения: поменять цвет текста, '
      'фона и добавить сетку в таблицу.'"\033[0m")



print("\033[4m\033[35m\033[43m"'Таблица умножения вариант 1')
for i in range(1,10):
    for j in range(1, 10):
        print(i * j, end='\t''|')
    print()

print("\033[4m\033[35m\033[40m"'Таблица умножения вариант 2')

for i in range(1, 10):
    for k in range(2, 10):
        print(f'{i} * {k} = {i * k}\t', end='|')
    print('')
else:
    print('')
# Дополнительный вариант!
from colorama import Fore, Back, Style

for i in range(1, 10):
    for j in range(1, 10):
        print(Back.GREEN + Fore.BLACK + str(i*j).center(5) + Style.RESET_ALL + "|", end='')

    print('\n' + '-'*55)


# Перемножить все нечётные значения в диапазоне от 1 до 100.
# Оформить таблицу умножения: поменять цвет текста, фона и добавить сетку в таблицу.