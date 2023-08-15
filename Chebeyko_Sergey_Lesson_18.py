#ДЗ на понедельник (Chebeyko_Sergey_18.py)
# Создайте класс BankAccount, который представляет банковский счет.
# У класса есть приватные свойства __account_number (номер счета) и __balance (баланс).
# Инициализатор __init__ используется для инициализации номера счета и начального баланса.
# Методы get_account_number и get_balance предоставляют доступ к приватным свойствам __account_number и __balance соответственно.
# Методы deposit и withdraw позволяют пополнять и снимать деньги со счета,
# при этом проверяя валидность операции (достаточно ли средств, корректно ли введена сумма для снятия).
# В основной части кода мы создаем экземпляр класса BankAccount с номером счета "123456789" и начальным балансом 1000.
# Затем мы используем методы для получения номера счета и баланса, а также для пополнения и снятия средств.
# Выводятся результаты операций.

class BankAccount:
    __account_number = None
    __balance = None

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        print('Номер счета: ', self.__account_number)

    def get_balance(self):
        print(f'Баланс: {self.__balance} Руб.')

    def deposit(self, deposit):
        self.__balance += deposit
        print(f'Вы успешно пополнили счет на {deposit} Руб. \nТекущий баланс: {self.__balance} Руб.')
    def withdraw(self, withdraw):
        if isinstance(withdraw, int) == True and self.__balance - withdraw >= 0:
            self.__balance -= withdraw
            print(f'Вы успешно вывели {withdraw} Руб. \nТекущий баланс: {self.__balance} Руб')
        else:
            print('Ошибка операции! ')

Bank_Client = BankAccount(123456789, 1000)

Bank_Client.get_account_number()
Bank_Client.get_balance()

command = ''
YorN = 'y'
while YorN != 'n':
    command = input('Пополнение( + ) / Вывод( - ) ')
    if command == '+':
        Bank_Client.deposit(int(input('Сколько Руб вы бы хотите внести: ')))
        YorN = input('Желаете продолжить?( Y/N )')
    elif command == '-':
        Bank_Client.withdraw(int(input('Сколько Руб вы бы хотите вывести: ')))
        YorN = input('Желаете продолжить?( Y/N )')
    else:
        print('Ошибка ввода!')
        YorN = input('Желаете продолжить?( Y/N )')
    if YorN.lower() == 'n':
        print('Операция завершена!\nЗаберите карту!:)')
        break
    elif YorN.lower() != 'y':
        print('Неизвестная команда!')
        YorN = input('Желаете продолжить?( Y/N )')
