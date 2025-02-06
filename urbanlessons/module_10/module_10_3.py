import threading
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.Lock = threading.Lock()

    def deposit(self):
        try:
            # if self.Lock.locked()==True:
            #     self.Lock.release()
            for operation in range(100):
                cash = randint(50, 500)
                self.balance += cash
                # print(self.Lock.locked())
                if self.balance >= 500 and self.Lock.locked() == True:
                    self.Lock.release()
                print(f"Пополнение: {cash}. Баланс: {self.balance}")
        except Exception as e:
            print(f'{e}')
    def take(self):
        for operation in range(100):
            try:
                if self.Lock.locked() == True:
                    self.Lock.release()
                cash = randint(50, 500)
                print(f'Запрос на {cash}')
                if cash < self.balance:
                    self.balance -= cash
                    print(f'Снятие: {cash}. Баланс:{self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
                    self.Lock.acquire()
            except Exception as e:
                    print(f'{e}')


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()