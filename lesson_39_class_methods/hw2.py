"""
    Создайте класс BankAccount для представления банковского счета. Класс должен
    иметь атрибуты account_number (номер счета) и balance (баланс), а также
    методы deposit() для внесения денег на счет и withdraw() для снятия денег со
    счета. Затем создайте экземпляр класса BankAccount, внесите на счет некоторую
    сумму и снимите часть денег. Выведите оставшийся баланс. Не забудьте
    предусмотреть вариант, при котором при снятии баланс может стать меньше нуля.
    В этом случае уходить в минус не будем, вместо чего будем возвращать сообщение
    "Недостаточно средств на счете".
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Неверная сумма. Операция не выполнена")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Недостаточно средств на счете")
        else:
            self.balance -= amount


my_acc = BankAccount("DE19996459960", 1000)
my_acc.deposit(400)
my_acc.withdraw(300)
my_acc.withdraw(650)
print(f"Остаток на счете {my_acc.account_number} составляет {my_acc.balance}")

