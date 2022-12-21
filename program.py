import tabulate

def user(): # Страница пользователя
        print ("Это страница пользователя")
        spisok()
def spisok(): # Страница товаров
        print(" Список всех товаров: ")
        from tabulate import tabulate
        data = []
        with open('list.txt',encoding="utf-8") as f: #открытие файла и добавление формата
            for line in f:
             data.append(list(map(str.strip, line.split(',')))) #сама табуретка
        print(tabulate(data, tablefmt='heavy_grid', headers=('Товар', 'Цена'))) #формат и что будет написано

#Страница добавления товаров
def additem(Item=None, Prise=None):
        Item = input("Введи название Товара: ")
        Prise = input("Введи цену товара: ")
        list = open("list.txt", "a", encoding="utf-8")                       # Открывает список товаров и ставит кадировку
        list.write(Item+", "+str(Prise)+"\n")     #записывает товар и цену в файл
        print("Товар успешно добавлен!")
        list.close()                              #сохраняет и закрывает
        admin()                                # кидает обратно в меню админа

#страница удаления товара
def removeitem(Item1=None):
    spisok()
    Item1 = input ("Напиши что ты бы хотел удалить: ")
    fn = 'list.txt'   #открывает лист
    f = open(fn, encoding="utf-8")
    output = []
    for line in f:
     if not Item1 in line:      #удаляет Item1
          output.append(line)
    f.close()          #закрывает лист
    f = open(fn, 'w', encoding="utf-8")
    f.writelines(output)
    f.close()
    print('''Ты удалил предмет! Возвращение на главную страницу...
    
    
    ''')
    admin()

#Страница редактирования товара
#По факту он удаляет предмет и заново добавляет
def replase(Newitem=None, NewName=None, Newprise=None):
    spisok()
    Newitem = input ("Напиши что ты бы хотел изменить: ")
    fn = 'list.txt' #открывает лист
    f = open(fn, encoding="utf-8")
    output = []
    for line in f:
        if not Newitem in line:      #удаляет newitem
            output.append(line)
    f.close()          #закрывает лист
    f = open(fn, 'w' , encoding="utf-8")
    f.writelines(output)
    f.close()

    NewName = input("Введи новое название товара: ")
    Newprise = input("Введи новую цену товара: ")
    list = open("list.txt", "a", encoding="utf-8")                       # Открывает список товаров и ставит кадировку
    list.write(NewName+", "+str(Newprise)+"\n")     #записывает товар и цену в файл
    print("Товар успешно изменён!")
    list.close()                              #сохраняет и закрывает
    admin()                           # кидает обратно в меню админа


def admin(): # Главная страница админа
    print('''Добро пожаловать в пункт управления администатора! Выберите пункт меню:
    1. Добавить товар
    2. Удалить товар
    3. Редактировать товар
    4. Просмотреть товар ''')
    user_input = input()
    if user_input == '1':
        additem()
    elif user_input == '2':
        removeitem()
    elif user_input == '3':
        replase()
    elif user_input == '4':
        spisok()
        admin()
    else:
        print("Ты что-то не так написал!")

def login(Username=None, Password=None): # Страница логирования
    Username = input("Введи свой логин: ")
    Password = input("Введи свой пароль: ")

    if not len(Username or Password) < 1: # Проверка логина и пароля
        db = open("database.txt", "r")  # Сравниние из БД
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            c = a, b
            d.append(a)
            f.append(b)
            data = dict(zip(d, f))
            if Username in data:
                if data[Username][0] == 'a': #  Админ
                    hashed = data[Username].strip('a')
                else:
                    hashed = data[Username].strip('b') # Юсер
                hashed = hashed.replace("'", "")
                hashed = hashed.encode('utf-8')

                if (Password.encode(), hashed):
                    print("Login success!")
                    print("Привет", Username,"!")
                    if data[Username][0] == 'a': # Если Админ, то кидает в строку админа
                        admin()
                    else:                        # Если не админ, то кидает в юсера
                        user()

                    break
                else:  # Если не всё ок, то пишет следующее:
                    print("Не правильный пароль!")
        if Username not in data:
            print("Такого логина не существует!")
    else:
        print("Пожалуйста, попробуйте войти ещё раз!")
        login()
    db.close() #закрываем бд
    # Страница регистрации
def register(Username=None, Password1=None, Password2=None):
    Username = input("Введите логин: ")
    Password1 = input("Придумайте пароль: ")
    Password2 = input("Подтвердите пароль: ")
    db = open("database.txt", "r")
    d = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        c = a,b
        d.append(a)
    if not len(Password1)<=3:                                # Нужно минимум 3 символа для регистрации
        db = open("database.txt", "r")
        if not Username ==None:
            if len(Username) <1:                              #Нужно минимум 1 символ для логина
                print("Пожалуйста укажите логин: ")
                register()
            elif Username in d:
                print("Этот логин занят!")                 # Если такой логин уже есть в БД
                register()
            else:
                if Password1 == Password2:                              # Шифрует БД
                    Password1 = Password1


                    db = open("database.txt", "a")                       # Записывает в БД регистрацию
                    db.write(Username+", "+str(Password1)+"\n")
                    print("Ваш аккаунт успешно создан!!!")
                    print("Пожалуйста, войдите чтобы продолжить.")


                # Если неправильно
                else:
                    print("Пароли не совпадают!")
                    register()
    else:
        print("Ваш пароль слишком короткий!!!")
    db.close() #нужно обазятельно закрывать бд, ибо если офф прогу то бд умрёт



def home(option=None):                                       # Главная страница
    print('''Добро пожаловать! Выберите пункт меню:
    1. Регистрация
    2. Вход''')
    user_input = input()
    if user_input == '1':
        register()
    elif user_input == '2':
        login()
    else:
        print("Ты ввел не то! Введи 1 или 2.")

# Регистрация(Логин, Пароль1, Пароль2)
# Авторизация(Логин, Пароль1)
home()