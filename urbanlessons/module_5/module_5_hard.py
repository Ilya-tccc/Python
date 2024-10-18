from time import sleep


class Video:
    time_now = 0

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __contains__(self, item):
        return self.nickname

class UrTube():
    users = []
    videos = []

    #   Непонятно как работает данное переопределение, т.к. у меня оно вообще не работает
        # def __contains__(self,item):
    #     if isinstance(item,User) and item.nickname in [user.nickname for user in self.users]:
    #         return True
    #     if isinstance(item,Video):
    #         return item.title in [video.title for video in self.videos]
    #     else:
    #         return False
    def __init__(self, current_user=None):
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            # print(hash(password),user.password, password,user.nickname,nickname)
            # if hash(password) == hash(user.password[nickname]):
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = nickname
                # print('Вход выполнен')
                break
        if self.current_user!=nickname:
            print("Пользователь не найден")


    def register(self, nickname, password, age):
        # if self.users==[]:
        #     self.users.append(User(nickname, password, age))
        #     self.log_in(nickname, password)
        if nickname not in [user.nickname for user in self.users]:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
             print(f"Пользователь {nickname} уже существует")
        # else:
        #     for user in self.users:
        #         # print(user.nickname,nickname)
        #         if nickname!=user.nickname:
        #             self.users.append(User(nickname, password, age))
        #             self.log_in(nickname, password)
        #         else:
        #             print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *others):
        for video in others:
            self.videos.append(video)

    def get_videos(self, title):
        list_=[]
        for video in self.videos:
            if str(title).upper() in str(video.title).upper():
                list_.append(video.title)
        return list_


    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if title == video.title:
                    for user in self.users:
                        # print(user.nickname, self.current_user)
                        if (user.nickname == self.current_user and video.adult_mode == True and user.age > 18) or (
                                user == self.current_user and user.adult_mode == False):
                            for second in range(int(video.duration)):
                                print(second, end=' ')
                                sleep(1)
                            print("Конец видео")
                        elif user.nickname == self.current_user and video.adult_mode == True and user.age < 18 :
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
    def users_info(self):
        for user in self.users:
            print(f"Пользователь {user.nickname}, пароль {user.password}, возраст {user.age} ")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupn', 'lolkekcheburek', 13)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
