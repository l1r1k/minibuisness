import os
from datetime import datetime
import pathlib
import sys
from pathlib import Path
import time
import smtplib
import json
import random
from email.mime.text import MIMEText

class User:
    def __init__(self, id_user: int, email_user: str, password_user: str, balance_user: int, type_user: str = "User", card_loyalty: str = 'Нету', spends_money: int = 0):
        self.id_user = id_user
        self.email_user = email_user
        self.password_user = password_user
        self.balance_user = balance_user
        self.type_user = type_user
        self.card_loyalty = card_loyalty
        self.spends_money = spends_money

class Buy_History:
    def __init__(self, id_buy_history: int, user_id: int, order_body: dict, final_cost: int):
        self.id_buy_history = id_buy_history
        self.user_id = user_id
        self.order_body = order_body
        self.final_cost = final_cost

class Coffee:
    def __init__(self, id_coffee: int, ingredients: dict, cost_coffee: int):
        self.id_coffee = id_coffee
        self.ingredients = ingredients
        self.cost_coffee = cost_coffee

class Toppings:
    def __init__(self, id_topping: int, topping_name: str, topping_cost: int):
        self.id_topping = id_topping
        self.topping_name = topping_name
        self.topping_cost = topping_cost

class Warehouse:
    def __init__(self, id_warehouse: int, ingredients: dict):
        self.id_warehouse = id_warehouse
        self.ingredients = ingredients

class Specials:
    def __init__(self, name_specials: str, rules_specials: str, count_for_sale: int, procent_sale: int):
        self.name_specials = name_specials
        self.rules_specials = rules_specials
        self.count_for_sale = count_for_sale
        self.procent_sale = procent_sale

def send_code(email, code):
    sender = "smallbuisnesspython@gmail.com"
    # fkfseqdrfseafybs
    password = "fkfseqdrfseafybs"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
    except:
        sys.exit('Нет подключения к интернету!')

    try:
        server.login(sender, password)
        msg = MIMEText(f"Код подтверждения почты: {code}\nВведите его для подтверждения почты в малом предприятии по изготовлению кофе.\nЕсли вы не имеете понятия о данном предприятии и ничего не производили, то напишите на данную почту: smallbuisnesspython@gmail.com")
        msg["Subject"] = "Код подтверждения"
        server.sendmail(sender, email, msg.as_string())

        return f"Код подтверждения был отправлен на почту {email}. Проверьте, пожалуйста, новые сообщения. Если сообщение не было обнаружено, то проверьте папку Спам!"
    except Exception as error:
        return "Ошибка!"
    
def registration(users_list):
    os.system('cls||clear')
    successful_registration = False
    while successful_registration == False:
        try:
            type_registration = int(input('Вы намерены работать у нас или быть покупателем? Введите 1, если покупателем или 2, если работать! '))
        except:
            print('Ошибка! Вы ввели не число! Попробуйте еще раз.')
            type_registration = 0
        match type_registration:
            case 1:
                id_user = random.randint(100000, 999999)
                while True:
                    email_user = input('Введите вашу почту: ')
                    check_unique = True
                    for item in users_list:
                        if item['email_user'] == email_user:
                            check_unique = False
                            print('Пользователь с такой почтой уже существует, укажите другую!')
                    if email_user.find('@') != -1 and email_user.find('.') != -1 and check_unique == True:
                        while True:
                            code = random.randint(111111, 999999)
                            response = send_code(email_user, code)
                            if response != "Ошибка!":
                                print(response)
                                try:
                                    input_code = int(input('Введите код, который получили в сообщении: '))
                                except:
                                    print('Вы ввели не число')
                                if code == input_code:
                                    print('Почта успешно подтверждена!')
                                    break
                            else:
                                print('Отправленный код и введенный не совпадают, подождите 5 секунд для повтора')
                                time.sleep(5)
                        break
                    else:
                        print('Неверный формат почты')
                password_user = input('Введите пароль для аккаунта: ')
                user_contructor = User(id_user, email_user, password_user, 0)
                users_list.append(user_contructor.__dict__)
                user_write = json.dumps(users_list, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
                Path('user.json').write_text(user_write, encoding="utf-8")
                successful_registration = True
                print('Регистрация пройдена')
            case 2:
                special_code = 'CoffeBreak'
                input_special_code = input('Для регистрации аккаунта сотрудника введите код, который вам сказал администратор: ')
                if input_special_code == special_code:
                    id_user = random.randint(100000, 999999)
                    while True:
                        email_user = input('Введите вашу почту: ')
                        check_unique = True
                        for item in users_list:
                            if item['email_user'] == email_user:
                                check_unique = False
                                print('Пользователь с такой почтой уже существует, укажите другую!')
                                break
                        if email_user.find('@') != -1 and email_user.find('.') != -1 and check_unique == True:
                            while True:
                                code = random.randint(111111, 999999)
                                response = send_code(email_user, code)
                                if response != "Ошибка!":
                                    print(response)
                                    try:
                                        input_code = int(input('Введите код, который получили в сообщении: '))
                                    except:
                                        print('Вы ввели не число')
                                    if code == input_code:
                                        print('Почта успешно подтверждена!')
                                        break
                                else:
                                    print('Отправленный код и введенный не совпадают, подождите 5 секунд для повтора')
                                    time.sleep(5)
                            break
                        else:
                            print('Неверный формат почты')
                    password_user = input('Введите пароль для аккаунта: ')
                    user_contructor = User(id_user, email_user, password_user, 0, type_user='Admin')
                    users_list.append(user_contructor.__dict__)
                    user_write = json.dumps(users_list, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
                    Path('user.json').write_text(user_write, encoding="utf-8")
                    successful_registration = True
                    print('Регистрация пройдена')
            case _:
                print('Ошибка! Введена неизвестная команда')

def authorization(users_list):
    os.system('cls||clear')
    email_user = input('Введите почту, которую указывали при регистрации: ')
    password_user = input('Введите пароль, который указывали при регистрации аккаунта: ')
    for item in users_list:
        if item['email_user'] == email_user and item['password_user'] == password_user:
            while True:
                code = random.randint(111111, 999999)
                response = send_code(email_user, code)
                if response != "Ошибка!":
                    print(response)
                    try:
                        input_code = int(input('Введите код, который получили в сообщении: '))
                    except:
                        print('Вы ввели не число')
                    if code == input_code:
                        print('Личность подтверждена!')
                        break
                    else:
                        print('Отправленный код и введенный не совпадают, подождите 5 секунд для повтора')
                        time.sleep(5)
            return item
    print('Неверный логин или пароль!')

def history(buy_history, user_id):
    for item in buy_history:
        if item['user_id'] == user_id:
            id_buy_history = item['id_buy_history']
            print(f'Номер заказа: {id_buy_history}')
            dict_items = item['order_body']
            name_coffe = list(dict_items.keys())
            print(f'Кофе - {name_coffe[0]}')

            print('Добавленные топинги: ')
            for items in dict_items:
                print(items)
            final_cost = item['final_cost']
            print(f'Итоговая цена заказа: {final_cost}\n')
            print('------------------------------------------------------')
        else:
            print('Пользователь не найден.')

def user_screen(users, user, toppings, coffee, buy_history, specials):
    while True:
        os.system('cls||clear')
        read_users = Path('user.json').read_text(encoding="utf-8")
        read_toppings = Path('toppings.json').read_text(encoding="utf-8")
        read_coffee = Path('coffee.json').read_text(encoding="utf-8")
        read_buy_history = Path('buy_history.json').read_text(encoding="utf-8")
        read_specials = Path('specials.json').read_text(encoding="utf-8")
        users = json.loads(read_users)
        toppings = json.loads(read_toppings)
        coffee = json.loads(read_coffee)
        buy_history = json.loads(read_buy_history)
        specials = json.loads(read_specials)
        id_user = user['id_user']
        email_user = user['email_user']
        balance_user = user['balance_user']
        card_loyalty = user['card_loyalty']
        spends_money = user['spends_money']
        if 5000 < spends_money > 10000:
            card_loyalty = 'Бронзовая карта'
        elif 10000 < spends_money > 15000:
            card_loyalty = 'Серебрянная карта'
        elif 15000 < spends_money > 25000:
            card_loyalty = 'Золотая карта'
        try:
            name_special = specials['name_specials']
            rules_special = specials['rules_specials']
            count_special = specials['count_for_sale']
            procent_special = specials['procent_sale']
        except:
            name_special = 'Отсутствует'
            rules_special = 'Отсутствует'
            procent_special = 0
        print(f'Здравствуйте, {email_user}! Акция на текущий момент: {name_special}! Условия: {rules_special}. Количество: {count_special}. Скидка: {rules_special if procent_special == 0 else procent_special}%')
        print(f'Ваш баланс: {balance_user}')
        print(f'Ваша карта лояльности: {card_loyalty}')
        print(f'Всего потрачено денег: {spends_money}')
        choose_func = input('Выберите действие, которое хотите произвести, 1 - Оформить заказ, 2 - Просмотреть историю покупок, 3 - Выйти из аккаунта: ')
        match choose_func:
            case '1':
                print('Ассортимент кофе:')
                final_cost_coffee = 0
                name_choosen_coffee = ''
                cost_choosen_coffee = 0
                coffees = {}
                for item in coffee:
                    list_coffee = item['ingredients']
                    coffee_cost = item['cost_coffee']
                    id_coffee = item['id_coffee']
                    for ingredient in list_coffee:
                        print(f'{id_coffee}. {ingredient} - {coffee_cost} руб.')
                        coffees[id_coffee] = [ingredient, coffee_cost]
                choosen_available_coffee = False
                while choosen_available_coffee == False:
                    try:
                        choose_coffee = int(input('Выберите кофе, введя цифру, которая указана перед ним: '))
                        if choose_coffee in coffees.keys():
                            choosen_available_coffee = True
                            list_choosen_coffee = coffees[choose_coffee]
                            name_choosen_coffee = list_choosen_coffee[0]
                            cost_choosen_coffee = list_choosen_coffee[1]
                            final_cost_coffee += list_choosen_coffee[1]
                        else:
                            print('Указанного кофе нет!') 
                    except Exception as error:
                        print('Ошибка, введено не число')
                        print(error)
                all_toppings = {}
                for topping in toppings:
                    id_topping = topping['id_topping']
                    name_topping = topping['topping_name']
                    cost_topping = topping['topping_cost']
                    print(f'{id_topping}. {name_topping} - {cost_topping} руб.')
                    all_toppings[id_topping] = [name_topping, cost_topping]
                all_choosen_toppings = []
                choosen_available_topping = False
                while choosen_available_topping == False:
                    try:
                        choose_topping = int(input('Выберите топпинг для вашего кофе, указав цифру, которая указана перед ним: '))
                        if choose_topping in all_toppings.keys():
                            correct_action = False
                            list_choosen_toppings = all_toppings[choose_topping]
                            all_choosen_toppings.append(f'{list_choosen_toppings[0]} - {list_choosen_toppings[1]} руб.')
                            final_cost_coffee += list_choosen_toppings[1]
                            while correct_action == False:
                                pass_input = input('Хотите еще топпинги или нет? 1 - да, 2 - нет: ')
                                match pass_input:
                                    case '1':
                                        correct_action = True
                                        pass
                                    case '2':
                                        correct_action = True
                                        choosen_available_topping = True
                                        pass
                                    case _:
                                        print('Такого выбора нет.')
                    except:
                        print('Ошибка, введено не число')
                correct_count_coffee = False
                while correct_count_coffee == False:
                    try:
                        count_coffee = int(input('Введите сколько кофе хотите: '))
                        correct_count_coffee = True
                    except:
                        print('Введено не число!')
                final_cost_coffee *= count_coffee
                our_chance_drop_hair = 5
                is_found_hair = False
                if our_chance_drop_hair == 5:
                    print('*Пользователь не видит это сообщение* Волос попал в стакан кофе!')
                    user_chance_found_hair = 5
                    if user_chance_found_hair == 5:
                        print('Пользователь обнаружил волос в своей чашке!!!! Предоставлена скидка в размере 30%!')
                        final_cost_coffee = final_cost_coffee * 0.7
                        is_found_hair = True
                    else:
                        print('Пользователь не обнаружил волос!')
                
                if card_loyalty == 'Бронзовая карта':
                    print('Была применена скидка карты лояльности в размере 5%!')
                    time.sleep(2)
                    final_cost_coffee *= 0.95
                elif card_loyalty == 'Серебрянная карта':
                    print('Была применена скидка карты лояльности в размере 10%!')
                    time.sleep(2)
                    final_cost_coffee *= 0.9
                elif card_loyalty == 'Золотая карта':
                    print('Была применена скидка карты лояльности в размере 15%!')
                    time.sleep(2)
                    final_cost_coffee *= 0.85

                if count_coffee >= count_special:
                    print(f'Была применена {name_special}')
                    time.sleep(2)
                    final_cost_coffee *= 1 - procent_special / 100

                print(f'Итоговая цена заказа - {final_cost_coffee}')

                if balance_user < final_cost_coffee:
                    print('Недостаточно средств... отмена заказа!')
                else:
                    spends_money += final_cost_coffee
                    balance_user -= final_cost_coffee
                    id_buy_history = random.randint(100000, 999999)
                    order_body = {f'{name_choosen_coffee} - {cost_choosen_coffee} руб.': all_choosen_toppings}
                    buy_history_constructor = Buy_History(id_buy_history, id_user, order_body, final_cost_coffee)
                    buy_history.append(buy_history_constructor.__dict__)
                    buy_history_write = json.dumps(buy_history, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
                    Path('buy_history.json').write_text(buy_history_write, encoding="utf-8")
                    user['balance_user'] = balance_user
                    user['card_loyalty'] = card_loyalty
                    user['spends_money'] = spends_money
                    for index, item in enumerate(users):
                        if item['id_user'] == user['id_user']:
                            users[index] = user
                    for index, item in enumerate(users):
                        if item['type_user'] == 'Admin':
                            item['balance_user'] += final_cost_coffee
                            users[index] = item
                    user_write = json.dumps(users, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
                    Path('user.json').write_text(user_write, encoding="utf-8")
                    check_string = 'ЧЕК ОБ ОПЛАТЕ!\n'
                    check_string += 'Маленькая Кофейня\n'
                    listcofee = list(order_body.keys())
                    if is_found_hair == True:
                        check_string += 'Волос баристы\n'
                    check_string += f'{listcofee[0]}\n'
                    check_string += 'Добавленные топинги: \n'
                    for item in order_body[f'{name_choosen_coffee} - {cost_choosen_coffee} руб.']:
                        check_string += f'{item}\n'
                    check_string += f'Количество: {count_coffee}\n'
                    check_string += f'Итого: {final_cost_coffee} руб.\n'
                    check_string += f'Дата заказа: {datetime.today().day}.{datetime.today().month}.{datetime.today().year}. Время заказа: {datetime.now().time().hour}:{datetime.now().time().minute}'
                    Path(f'check{id_buy_history}.txt').write_text(check_string, encoding="utf-8")
                smth_for_pass = input('Введите что-либо, чтобы продолжить: ')
            case '2':
                print('------------------------------------------------------')
                history(buy_history, id_user)
                smth_for_exit = input('Введите что-то, чтобы вернутья в меню: ')
            case '3':
                print('Выход из аккаунта...')
                time.sleep(2)
                return 0
            case _:
                print('Ошибка! Выбранное действие не существует!')

def admin_screen(user, users, warehouse, toppings, coffee, buy_history, specials):
    while True:
        os.system('cls||clear')
        read_users = Path('user.json').read_text(encoding="utf-8")
        read_warehouse = Path('warehouse.json').read_text(encoding="utf-8")
        read_toppings = Path('toppings.json').read_text(encoding="utf-8")
        read_coffee = Path('coffee.json').read_text(encoding="utf-8")
        read_buy_history = Path('buy_history.json').read_text(encoding="utf-8")
        read_specials = Path('specials.json').read_text(encoding="utf-8")
        users = json.loads(read_users)
        warehouse = json.loads(read_warehouse)
        toppings = json.loads(read_toppings)
        coffee = json.loads(read_coffee)
        buy_history = json.loads(read_buy_history)
        specials = json.loads(read_specials)
        id_user = user['id_user']
        email_user = user['email_user']
        balance_user = user['balance_user']
        card_loyalty = user['card_loyalty']
        spends_money = user['spends_money']
        try:
            name_special = specials['name_specials']
            rules_special = specials['rules_specials']
            count_special = specials['count_for_sale']
            procent_special = specials['procent_sale']
        except:
            name_special = 'Отсутствует'
            rules_special = 'Отсутствует'
            procent_special = 0
        print(f'Здравствуйте, {email_user}! Акция на текущий момент: {name_special}! Условия: {rules_special}. Количество: {count_special}. Скидка: {rules_special if procent_special == 0 else procent_special}')
        print(f'Ваш баланс: {balance_user}')
        choose_func = input('Выберите действие, которое хотите произвести, 1 - Собрать блюдо, 2 - Просмотреть историю покупок пользователя, 3 - Проверить склад, 4 - Акция, 5 - Выйти из аккаунта: ')
        match choose_func:
            case '1':
                name_coffee = input('Введите название для вашего кофе: ')
                ingredients = []
                print('Ингредиенты:')
                i = 0
                for item in warehouse:
                    ingredients_dict = item['ingredients']
                    for items in ingredients_dict:
                        list_in_dict = ingredients_dict[items]
                        print(f'{i}. {items} - {list_in_dict[0]} шт. {list_in_dict[1]}руб.')
                        i += 1
                        ingredients.append(items)
                all_choosen_ingredients = []
                choosen_available_ingredients = False
                while choosen_available_ingredients == False:
                    try:
                        choose_ingredients = int(input('Выберите ингредиент для вашего кофе, указав цифру, которая указана перед ним: '))
                        if 0 <= choose_ingredients < len(ingredients):
                            correct_action = False
                            all_choosen_ingredients.append(ingredients[choose_ingredients])
                            while correct_action == False:
                                pass_input = input('Хотите добавить еще ингредиентов или нет? 1 - да, 2 - нет: ')
                                match pass_input:
                                    case '1':
                                        correct_action = True
                                        pass
                                    case '2':
                                        correct_action = True
                                        choosen_available_ingredients= True
                                        pass
                                    case _:
                                        print('Такого выбора нет.')
                    except:
                        print('Ошибка, введено не число')
                ingredients_coffe = {name_coffee: all_choosen_ingredients}
                while True:
                    try:
                        cost_coffee = int(input('Укажите цену для вашего кофе: '))
                        break
                    except:
                        print('Не число!')
                for index, item in enumerate(coffee):
                        if item['id_coffee'] == 1:
                            item['ingredients'] = ingredients_coffe
                            item['cost_coffee'] = cost_coffee
                            coffee[index] = item
                coffee_write = json.dumps(coffee, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
                Path('coffee.json').write_text(coffee_write, encoding="utf-8")

            case '2':
                try_found_user = False
                while try_found_user == False:
                    input_email = input('Введите почту покупателя: ')
                    for item in users:
                        if item['email_user'] == input_email:
                            if item['type_user'] == 'User':
                                user_id = item['id_user']
                                try_found_user = True
                                break
                            else:
                                print('Пользователь должен быть покупателем!')
                    print('Покупатель не найден, введите почту корректно!')
                print('------------------------------------------------------')
                history(buy_history, user_id)
                for item in users:
                    if item['id_user'] == user_id:
                        card_loyalty_user = item['card_loyalty']
                print(f'\nКарта лояльности покупателя: {card_loyalty_user}')
                smth_for_exit = input('Введите что-то, чтобы вернутья в меню: ')
            case '3':
                for item in warehouse:
                    ingredients_dict = item['ingredients']
                    for items in ingredients_dict:
                        list_in_dict = ingredients_dict[items]
                        print(f'{items} - {list_in_dict[0]} шт. {list_in_dict[1]}руб.')
                smth_for_exit = input('Чтобы вернуться назад в меню - введите что угодно.')  
            case '4':
                name_specials_input = input('Введите название акции: ')
                rules_specials_input = input('Введите правила акции: ')
                while True:
                    try:
                        count_for_sale = int(input('Введите количество товаров, которое необходимо купить для получения скидки: '))
                        procent_sale = int(input('Введите процент скидки (только число!): '))
                        break
                    except:
                        print('Не число!')
                special_discount = Specials(name_specials_input, rules_specials_input, count_for_sale, procent_sale)
                specials_write = json.dumps(special_discount.__dict__, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
                Path('specials.json').write_text(specials_write, encoding="utf-8")
                print('Акция создана!')
                time.sleep(2)
            case '5':
                print('Выход из аккаунта...')
                time.sleep(2)
                return 0
            case _:
                print('Ошибка! Выбранное действие не существует!')

def main():
    users = {}
    warehouse = {}
    toppings = {}
    coffee = {}
    buy_history = {}
    while True:
        if os.path.exists('user.json') and os.path.exists('warehouse.json') and os.path.exists('toppings.json') and os.path.exists('coffee.json') and os.path.exists('buy_history.json') and os.path.exists('specials.json'):
            try:
                read_users = Path('user.json').read_text(encoding="utf-8")
                read_warehouse = Path('warehouse.json').read_text(encoding="utf-8")
                read_toppings = Path('toppings.json').read_text(encoding="utf-8")
                read_coffee = Path('coffee.json').read_text(encoding="utf-8")
                read_buy_history = Path('buy_history.json').read_text(encoding="utf-8")
                read_specials = Path('specials.json').read_text(encoding="utf-8")
            except Exception as error:
                print(error)
        else:
            user_file = Path('user.json')
            warehouse_file = Path('warehouse.json')
            toppings_file = Path('toppings.json')
            coffee_file = Path('coffee.json')
            buy_history_file = Path('buy_history.json')
            specials_file = Path('specials.json')
            user_file.touch(exist_ok=True)
            warehouse_file.touch(exist_ok=True)
            toppings_file.touch(exist_ok=True)
            coffee_file.touch(exist_ok=True)
            buy_history_file.touch(exist_ok=True)
            specials_file.touch(exist_ok=True)
        try:
            users = json.loads(read_users)
            warehouse = json.loads(read_warehouse)
            toppings = json.loads(read_toppings)
            coffee = json.loads(read_coffee)
            buy_history = json.loads(read_buy_history)
            specials = json.loads(read_specials)
        except Exception as error:
            print(error)
        os.system('cls||clear')
        choose_func = input('Хотите создать новый аккаунт или авторизоваться? 1 - регистрация, 2 - авторизация, 3 - завершить работу приложения: ')
        match choose_func:
            case '1':
                registration(users)
                user = authorization(users)
            case '2':
                user = authorization(users)
            case '3':
                print('Выход из приложенния...')
                time.sleep(2)
                os.system('cls||clear')
                sys.exit()
            case _:
                print('Ошибка! Введено неверное значение!')
        if user['type_user'] == 'User':
            for item in coffee:
                cost_coffee = item['cost_coffee']
            balance_user = cost_coffee + cost_coffee * (random.randint(20,40) / 100)
            user['balance_user'] += balance_user
            for index, item in enumerate(users):
                if item['id_user'] == user['id_user']:
                    users[index] = user
            user_write = json.dumps(users, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
            Path('user.json').write_text(user_write, encoding="utf-8")
            user_screen(users, user, toppings, coffee, buy_history, specials)
        elif user['type_user']  == 'Admin':
            admin_screen(user, users, warehouse, toppings, coffee, buy_history, specials)

if __name__ == "__main__":
    main()