print  ("Домашнее задание №4, Чебейко Сергей Леонидович")

print ('''1.Вводиться строка. Удалить из неё все пробелы. После этого определить, 
является ли она палиндромом(перевертышем), т.е. одинаково пишется, как сначала, так и с конца''')

s = input("user введите тест:   ")
s = s.replace(' ','')
s = s.lower()
print(s)
print(s[::-1])

if s == s[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")

print ("2.Дана строка (вводит пользователь), вывод строк символов")

a = "Малиновка" #строка user
# 1.Сначала выведите третий символ этой строки.
print("cтр. 1:", a [2])
# 2.Во второй строке выведите предпоследний символ этой строки.
print("стр. 2:", a[-2])
# 3.В третьей строке выведите первые пять символов этой строки.
print("стр. 3:", a[:5])
# 4.В четвертой строке выведите всю строку, кроме последних двух символов.
print("стр. 4:", a[:-2])
# 5.В пятой строке выведите все символы с четными индексами
# (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
print("стр. 5:", a[::2])
# 6.В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
print("стр. 6:", a[1::2])
# 7.В седьмой строке выведите все символы в обратном порядке.
print("стр. 7:", a[::-1])
# 8.В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
print("стр. 8:", a[-1::-2])
# 9.В девятой строке выведите длину данной строки.
print("стр. 9:", len(a))










