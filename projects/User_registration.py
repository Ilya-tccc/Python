from random import choice

from encodings.punycode import selective_find


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователей, содержащий атрибуты: логин и пароль.
    """

    def __init__(self, username, password, confirm_password):
        self.username = username
        self.password = self.check_password(username, password, confirm_password)
        # if password == confirm_password else print(
        # 'Введенные пароли отличаются. Повторите регистрацию')
        # if password==confirm_password:
        #     self.password=password

    def check_password(self, user, password1, password2):
        if password1 != password2:
            print(f'Введенные пароли отличаются. Повторите регистрацию \nЛогин {user1}')
            password1 = input('Введите пароль ')
            password2 = input('Подтвердите пароль ')
            return self.check_password(user, password1, password2)
        elif len(password1) < 8:
            print("Длинна пароля менее 8 символов. Повторите ввод")
            print(f'Логин {user1}')
            password1 = input('Введите пароль ')
            password2 = input('Подтвердите пароль ')
            return self.check_password(user, password1, password2)
        elif password1.isnumeric() or password1.islower() or password1.isupper() or password1.isalpha():  # проверки по порядку: только числа, только нижний, только верхний, только буквы. Нужно исправить, т.к. работает не идеально.
            print(
                "Пароль должен содержать хотя бы один символ, одну цифру и по одной букве в нижнем и верхнем регистре. Повторите ввод!")
            print(f'Логин {user1}')
            password1 = input('Введите пароль ')
            password2 = input('Подтвердите пароль ')
            return self.check_password(user, password1, password2)
        else:
            return password1


if __name__ == '__main__':
    database = Database()

    while True:
        choice = int(input('Приветствую! Выберите действие: \n 1 - Вход \n 2 - Регистрация \n '))
        if choice == 2:
            user = User(user1 := input('Введите логин '), password1 := input('Введите пароль '),
                        password2 := input('Подтвердите пароль '))
            # user.password[user1]=user.check_password(user1, password1, password2)
            # elif len(password1) < 8:
            #     print("Длинна пароля менее 8 символов. Повторите ввод")
            #     user = User(f'Логин {user1}', password1 := input('Введите пароль '),
            #                 password2 := input('Подтвердите пароль '))
            # elif password1.isnumeric() or password1.islower() or password1.isupper() or password1.isalpha():  # проверки по порядку: только числа, только нижний, только верхний, только буквы
            #     print(
            #         "Пароль должен содержать хотя бы один символ, одну цифру и по одной букве в нижнем и верхнем регистре. Повторите ввод!")
            database.add_user(user.username, user.password)
        elif choice == 1:
            user = User(login := input('Введите логин '), password1 := input('Введите пароль '), password1)
            if login in database:
                if database.data[login] == password1:
                    print(f'привет {login}')
                else:
                    print("Пароль введен неверно. Повторите ввод")
                    continue
        else:
            break

    print(database.data)
