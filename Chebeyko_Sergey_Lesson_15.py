#ДЗ на четверг (Chebeyko_Sergey_Lesson_15.py)
# №1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0
# №2. Привяжите к предыдущей функции декоратор, который будет выводить информацию о том,
# какой тип данных вы отправили: кортеж, список, число, строку или какой-то другой.


def function(fn):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f'Тип - {type(arg).__name__}!')

        return fn(*args, **kwargs)

    return wrapper

@function
def my_func(data):
    sum = 0
    col_b = 0
    col_ch = 0
    if isinstance(data, tuple):
        for el in data:
            if type(el) == str:
                sum += len(el)
        return print(f'Длина всех строк: {sum}')

    elif isinstance(data, list):
        for el in data:
            if type(el) == str:
                for i in el:
                    if i.isalpha():
                        col_b += 1
                    elif i.isdigit():
                        col_ch += 1
            else:
                col_ch += 1
        return print(f'Количество букв: {col_b}, количество чисел: {col_ch}')

    elif isinstance(data, int):
        data = str(data)
        col_nech = 0
        for i in range(len(data)):
            if int(data[i]) % 2 != 0:
                col_nech += 1
        return print(f'Количество нечетных цифр: {col_nech}')

    elif isinstance(data, str):
        return print(f'Длина строки: {len(data)}')


my_func((1,2,3,'a','bc8?',7,8,9))
my_func([1,2,3,'a','bc8?'])
my_func(783589)
my_func('7859989')