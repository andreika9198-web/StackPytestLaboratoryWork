from Class.my_class import User
# ■ Добавить нового пользователя
# ■ Удалить существующего пользователя
# ■ Проверить существует ли пользователь
# ■ Изменить логин существующего пользователя
# ■ Изменить пароль существующего пользователя

if __name__ == '__main__':
    user_obj = User()
    print('Работа с пользователем')
    while True:
        navigation = input(f"""
1.Добавить нового пользователя
2.Удалить существующего пользователя
3.Проверить существует ли пользователь
4.Изменить логин существующего пользователя
5.Изменить пароль существующего пользователя
6.Вывести список всех пользователей
Ваш вариант: """).strip()
        if navigation == '0':
            break
        elif navigation == '1':
            user_name = input("Введите имя пользователя: ").strip().capitalize()
            user_password = input("Введите пароль: ").strip()
            user_obj.add_user({"name": user_name, "password": user_password})
            print(f'Пользователь {user_name} был успешно добавлен')
        elif navigation == '2':
            user_name = input("Введите имя пользователя которого хотите удалить: ").strip().capitalize()
            if  user_obj.remove_user(user_name):
                print("Пользователь был удален")
            else:
                print("Пользователь не был удален")
        elif navigation == '3':
            user_name = input("Введите имя пользователя: ").strip().capitalize()
            user_obj.is_user(user_name)
        elif navigation == '4':
            user_name = input("Введите имя пользователя: ").strip().capitalize()
            new_user_name = input("Введите новое имя пользователя: ").strip().capitalize()
            user_obj.update_field(user_name,new_user_name,'name')
        elif navigation == '5':
            user_name = input("Введите имя пользователя: ").strip().capitalize()
            password_user = input("Введите новый пароль пользователя: ").strip()
            user_obj.update_field(user_name, password_user, "password")
        elif navigation == "6":
            user_obj.show()
        else:
            print("Такого варианта нету")