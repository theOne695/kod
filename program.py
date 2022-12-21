import tabulate

def user():
        print ("Это страница пользователя")
        spisok()
def spisok():
        print(" Список всех товаров: ")
        from tabulate import tabulate
        data = []
        with open('kod.txt',encoding="utf-8") as f:
            for line in f:
             data.append(list(map(str.strip, line.split(','))))
        print(tabulate(data, tablefmt='grid', headers=('Товар', 'Цена')))


def additem(Item=None, Prise=None):
        Item = input("Введи название Товара: ")
        Prise = input("Введи цену товара: ")
        list = open("kod.txt", "a", encoding="utf-8")
        list.write(Item+", "+str(Prise)+"\n")
        print("Товар успешно добавлен!")
        list.close()
        admin()


def removeitem(Item1=None):
    spisok()
    Item1 = input ("Напиши что ты бы хотел удалить: ")
    fn = 'kod.txt'   #открывает лист
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

def replase(Newitem=None, NewName=None, Newprise=None):
    spisok()
    Newitem = input ("Напиши что ты бы хотел изменить: ")
    fn = 'kod.txt'
    f = open(fn, encoding="utf-8")
    output = []
    for line in f:
        if not Newitem in line:
            output.append(line)
    f.close()
    f = open(fn, 'w' , encoding="utf-8")
    f.writelines(output)
    f.close()

    NewName = input("Введи новое название товара: ")
    Newprise = input("Введи новую цену товара: ")
    list = open("kod.txt", "a", encoding="utf-8")
    list.write(NewName+", "+str(Newprise)+"\n")
    print("Товар успешно изменён!")
    list.close()
    admin()


def admin():
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

    else:
        print("Ты что-то не так написал!")

def login(Username=None, Password=None):
    Username = input("Введи свой логин: ")
    Password = input("Введи свой пароль: ")

    if not len(Username or Password) < 1:
        db = open("database.txt", "r")
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
                if data[Username][0] == 'a':
                    hashed = data[Username].strip('a')
                else:
                    hashed = data[Username].strip('b') # Юсер
                hashed = hashed.replace("'", "")
                hashed = hashed.encode('utf-8')

                if (Password.encode(), hashed):
                    print("Login success!")
                    print("Привет", Username,"!")
                    if data[Username][0] == 'a':
                        admin()
                    else:
                        user()

                    break
                else:
                    print("Не правильный пароль!")
        if Username not in data:
            print("Такого логина не существует!")
    else:
        print("Пожалуйста, попробуйте войти ещё раз!")
        login()
    db.close()

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
    if not len(Password1)<=3:
        db = open("database.txt", "r")
        if not Username ==None:
            if len(Username) <1:
                print("Пожалуйста укажите логин: ")
                register()
            elif Username in d:
                print("Этот логин занят!")
                register()
            else:
                if Password1 == Password2:
                    Password1 = Password1


                    db = open("database.txt", "a")
                    db.write(Username+", "+str(Password1)+"\n")
                    print("Ваш аккаунт успешно создан!!!")
                    print("Пожалуйста, войдите чтобы продолжить.")

                else:
                    print("Пароли не совпадают!")
                    register()
    else:
        print("Ваш пароль слишком короткий!!!")
    db.close()



def home(option=None):
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

home()