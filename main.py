# pythonProject 9

# БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С РЕЦЕПТАМИ
# Бот получает список рецептов из файла, создает словарь и случайный рецепт (с рекламой!!!) и с фото блюда
# через случайные период времени постит в канал.
# Для этого нам нужно создать свой канал в Telegram,
# добавить в подписчики канала нашего бота и назначить его администратором канала с правом публиковать сообщения.
# Файл с рецептами должен лежать в папке data рядом со скриптом бота.

# $ pip install schedule - установить внешние зависимости

import telebot
import random
import time
import datetime

from config import token, channel

bot = telebot.TeleBot(token)

# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = channel


def open_text(path):
    """
    Загружает список с текстом из файла, выводит уведомление об удачной загрузке или ошибке
    :param path:путь к файлу в виде 'recipes1.txt'
    :return: список с текстовыми данными
    """
    try:
        # Загружаем список с текстом из файла
        try:  # этот блок не прерывает работу программы
            p = open(path, 'r', encoding='UTF-8')
            text_list = p.read().split('\n\n\n')
            print(f"Загружен файл \"{path}\" длиной {len(text_list)}")
        finally:
            p.close()  # и закрывает открытый файл если он не прочитался
    except FileNotFoundError:
        print(f"Невозможно открыть текстовый файл: {path}")
    except:
        print(f"Ошибка при работе с текстовым файлом: {path}")
    return text_list


# создаем словарь
def convert_to_dict(recipe_list):
    """
    Преобразуем список с рецептами в словарь
    :param recipe_list: список
    :return: словарь
    """
    d_recipes = {}
    for recipe in recipe_list:
        d_recipes[recipe[:recipe.index("\n\n")]] = recipe
    return d_recipes


def test():
    """
    Перебирает все блюда. Стаабильно обрабатывает 10-20 сообщений (использовать срезы списков).
    :return:  Выводит название блюда и длину сообщения
    """
    for recipe_name in recipe_names5:  # МЕНЯТЬ recipe_names1
        # Перебирем все блюда. Если выводит ошибку - попрововать сделать срез списка
        time.sleep(2)
        promo = random.choice(prom_list)  # реклама
        print(f"recipe_name: {recipe_name}, promo: {promo}")
        answer = d5_recipes[recipe_name]  # МЕНЯТЬ d1_recipes
        # выбираем рецепт из словаря по названию блюда
        if len(answer + '\n\n' + promo) < 1000:
            answer += '\n\n' + promo

        print("длина рецепта: ", len(answer))  # если длина более 1024, то картинку не закрепить
        try:
            try:  # этот блок не прерывает работу программы
                files = open(path_dict5[recipe_name], 'rb')  # МЕНЯТЬ path_dict1
                # открываем картинку
                bot.send_photo(CHANNEL_NAME, photo=files, caption=answer)  # посылаем ее и рецепт
            finally:
                files.close()  # и закрывает открытый файл если он не прочитался
        except FileNotFoundError:
            print("Невозможно открыть файл с изображением")
        except:
            print("Ошибка при работе с изображением")


def get_path(ind):
    """
    Определяет случайным образом из какой папки будут браться рецепты
    :return: словарь с рецептами, список с названиями блюд, словарь с путями к фото
    """
    # ind = random.randint(1, 5)
    if ind == 1:
        d_rec = d1_recipes
        recipe_n = recipe_names1
        path_d = path_dict1
    elif ind == 2:
        d_rec = d2_recipes
        recipe_n = recipe_names2
        path_d = path_dict2
    elif ind == 3:
        d_rec = d3_recipes
        recipe_n = recipe_names3
        path_d = path_dict3
    elif ind == 4:
        d_rec = d4_recipes
        recipe_n = recipe_names4
        path_d = path_dict4
    else:
        d_rec = d5_recipes
        recipe_n = recipe_names5
        path_d = path_dict5

    return d_rec, recipe_n, path_d


# Загружаем список с рекламными объявлениями и рецепты из файлов
prom_list = open_text('promotions.txt')
recipes1 = open_text('recipes1.txt')
recipes2 = open_text('recipes2.txt')
recipes3 = open_text('recipes3.txt')
recipes4 = open_text('recipes4.txt')
recipes5 = open_text('recipes5.txt')

# список1 с путями к фото {"название блюда":"путь к нему"}
path_dict1 = {"Фриттата с хлебом": "pictures1/pict1.jpg", 'Творожный смузи с бананом и какао': "pictures1/pict2.jpg",
              'Омлет в пароварке': "pictures1/pict3.jpg", 'Салат из щавеля с яйцом и огурцом': "pictures1/pict4.jpg",
              'Смузи с малиной и бананом': "pictures1/pict5.jpeg",
              'Малиновый смузи с бананом и черной смородиной': "pictures1/pict6.jpg",
              'Смузи с малиной, яблоком и грушей': "pictures1/pict7.jpeg",
              'Бутерброды со шпротами и творожным сыром': "pictures1/pict8.jpg",
              'Салат «Щетка» с редькой': "pictures1/pict9.jpg",
              'Салат «Оливье» с говядиной и свежими огурцами': "pictures1/pict10.jpg",
              'Сырные пончики': "pictures1/pict11.jpg", 'Смузи с ананасом и сельдереем': "pictures1/pict12.jpeg",
              'Шоколадный смузи с бананом и кокосовым молоком': "pictures1/pict13.jpg",
              'Салат из шпината и огурцов': "pictures1/pict14.jpeg",
              'Соус с кинзой и томатной пастой': "pictures1/pict15.jpeg",
              'Смузи с овсянкой и бананом': "pictures1/pict16.jpg", 'Чай из одуванчиков': "pictures1/pict17.jpeg",
              'Смузи с авокадо и сельдереем': "pictures1/pict18.jpg",
              'Гречка со стручковой фасолью': "pictures1/pict19.jpg",
              'Вкусное хрустящее тесто для чебуреков с водкой': "pictures1/pict20.jpg"
              }

# список2 с путями к фото {"название блюда":"путь к нему"}
path_dict2 = {'Салат с фасолью, ветчиной и сыром': "pictures2/pict1.jpg",
              'Печенье овсяное с медом': "pictures2/pict2.jpg", 'Блинчики с ветчиной и сыром': "pictures2/pict3.jpg",
              'Бутерброды с ананасом, ветчиной и сыром': "pictures2/pict4.jpg",
              'Паста с ветчиной и сыром': "pictures2/pict5.jpg",
              'Печенье творожное на скорую руку': "pictures2/pict6.jpg",
              'Салат «Дамский каприз» с языком и ветчиной': "pictures2/pict7.jpg",
              'Пирог с ветчиной и сыром': "pictures2/pict8.jpg", 'Кекс с тыквой': "pictures2/pict9.jpg",
              'Салат с ветчиной и яблоками': "pictures2/pict10.jpg",
              'Ленивая овсяная каша с апельсиновым джемом': "pictures2/pict11.jpg",
              'Веселые яблочки': "pictures2/pict12.jpg", 'Печенье с кокосовой стружкой': "pictures2/pict13.jpg",
              'Печенье с шоколадной крошкой': "pictures2/pict14.jpg", 'Печенье на йогурте': "pictures2/pict15.jpg",
              'Манная каша с тыквой': "pictures2/pict16.jpg", 'Печенье с джемом': "pictures2/pict17.jpg",
              'Соус с солеными огурцами': "pictures2/pict18.jpg",
              'Печенье из тыквы и овсяных хлопьев': "pictures2/pict19.jpeg",
              'Салат «Обжорка» с мясом и солеными огурцами': "pictures2/pict20.jpeg",
              'Филе куриное с шампиньонами в сливках': "pictures2/pict21.jpeg",
              'Каштаны, запеченные в духовке': "pictures2/pict22.jpg",
              'Яйца, фаршированные сыром и чесноком': "pictures2/pict23.jpg",
              'Филе куриное с помидорами и сыром': "pictures2/pict24.jpeg",
              'Быстрое печенье к чаю': "pictures2/pict25.jpg", 'Котлеты из минтая в духовке': "pictures2/pict26.jpg",
              'Спагетти с беконом': "pictures2/pict27.jpg", 'Котлеты на пару в сковороде': "pictures2/pict28.jpg",
              'Творожный десерт с порошковым желе': "pictures2/pict29.jpg",
              'Куриные бедра по-турецки': "pictures2/pict30.jpg", 'Котлеты диетические рыбные': "pictures2/pict31.jpg",
              'Кекс без масла и маргарина (на кефире)': "pictures2/pict32.jpg",
              'Рулетики с ветчиной, сыром и чесноком': "pictures2/pict33.jpeg",
              'Яйца, фаршированные тунцом': "pictures2/pict34.jpeg",
              'Шоколадный кекс на кефире без яиц': "pictures2/pict35.jpg",
              'Гречка с курицей и черносливом в горшочках': "pictures2/pict36.jpeg",
              'Рыба в яблочном соусе': "pictures2/pict37.jpeg", 'Торт из овсяного печенья': "pictures2/pict38.jpg",
              'Малиновое печенье с шоколадом (на сливочном масле)': "pictures2/pict39.jpg",
              'Торт с печеньем савоярди': "pictures2/pict40.jpeg", 'Сладкие помидоры на зиму': "pictures2/pict41.jpeg"}

# список3 с путями к фото {"название блюда":"путь к нему"}
path_dict3 = {'Котлеты картофельные с начинкой': "pictures3/pict1.jpg", 'Тирамису из печенья': "pictures3/pict2.jpg",
              'Куриное филе в фольге в духовке': "pictures3/pict3.jpeg",
              'Пирог из слоеного теста с рыбными консервами': "pictures3/pict4.jpg",
              'Пирог с консервированной сайрой': "pictures3/pict5.jpeg",
              'Куриные ножки в сметане в духовке': "pictures3/pict6.jpg", 'Соус «Цахтон»': "pictures3/pict7.jpeg",
              'Курица кусочками в духовке': "pictures3/pict8.jpeg",
              'Рыбные котлеты из камбалы в духовке для детей': "pictures3/pict9.jpeg",
              'Салат с авокадо и печенью трески': "pictures3/pict10.jpg",
              'Мятный соус на кефире': "pictures3/pict11.jpeg",
              'Слоеный салат с печенью трески': "pictures3/pict12.jpeg",
              'Фриттата со шпинатом и сыром': "pictures3/pict13.jpg",
              'Котлеты из гречки и творога': "pictures3/pict14.jpg", 'Тушёная курица с грибами': "pictures3/pict15.jpg",
              'Паштет из печени трески': "pictures3/pict16.jpg", 'Белая рыба в банке': "pictures3/pict17.jpg"}

# список4 с путями к фото {"название блюда":"путь к нему"}
path_dict4 = {'Куриное филе с грибами в сметанном соусе с паприкой': "pictures4/pict1.jpeg",
              'Молочный коктейль с мороженым и клубникой': "pictures4/pict2.jpeg",
              'Тесто на манты без яиц': "pictures4/pict3.jpg", 'Смузи из чёрной смородины': "pictures4/pict5.jpeg",
              'Яичный паштет с печенью трески и овощами': "pictures4/pict4.jpg",
              'Оладьи из кабачков без муки': "pictures4/pict6.jpg",
              'Лепёшки без дрожжей на сковороде': "pictures4/pict7.jpg", 'Малиновый коктейль': "pictures4/pict8.jpg",
              'Малосольные огурцы в пакете за 2 часа': "pictures4/pict9.jpeg",
              'Жареная картошка с хрустящей корочкой на сковороде': "pictures4/pict10.jpg",
              'Морс из чёрной смородины': "pictures4/pict11.jpg",
              'Варенье из красной смородины 5-минутка': "pictures4/pict12.jpeg",
              'Бисквитный пирог с клубникой': "pictures4/pict13.jpg", 'Жареные кабачки с яйцом': "pictures4/pict14.jpg",
              'Смузи «Клубничный чизкейк»': "pictures4/pict15.jpg",
              'Оладьи из кабачков с фаршем': "pictures4/pict16.jpg",
              'Сырники без муки и манки': "pictures4/pict17.jpg",
              'Красная рыба с картошкой в духовке': "pictures4/pict18.jpg",
              'Пельмени с сыром и сметаной в духовке': "pictures4/pict19.jpg",
              'Ванильно-шоколадные маффины с черешней': "pictures4/pict20.jpg",
              'Сырный суп с курицей и вермишелью': "pictures4/pict21.jpeg", 'Соус из кабачков': "pictures4/pict22.jpg",
              'Пышный омлет с сыром на сковороде': "pictures4/pict23.jpeg",
              'Малосольные огурцы за час': "pictures4/pict24.jpeg",
              'Варенье из облепихи «Пятиминутка»': "pictures4/pict25.jpeg",
              'Лаваш с корейской морковкой и ветчиной': "pictures4/pict26.jpg",
              'Сырники с бананом в духовке': "pictures4/pict27.jpg", 'Салат с жареными опятами': "pictures4/pict29.png",
              'Жареные кабачки с сыром и чесноком': "pictures4/pict28.jpg",
              'Гречка по-купечески с фаршем в мультиварке': "pictures4/pict30.jpeg",
              'Цукини, фаршированные мясом индейки и сыром': "pictures4/pict31.jpg",
              'Тефтели в духовке без подливы': "pictures4/pict32.jpg",
              'Морковные кексы с изюмом': "pictures4/pict33.jpeg"}

# список5 с путями к фото {"название блюда":"путь к нему"}
path_dict5 = {'Манник на сметане без муки': "pictures5/pict1.jpeg",
              'Маринованные кабачки по-корейски быстрого приготовления': "pictures5/pict2.jpeg",
              'Классический гуляш из свинины': "pictures5/pict3.jpg",
              'Яблочно-грушевый сок на зиму': "pictures5/pict4.jpeg",
              'Сырники с бананом и медом': "pictures5/pict5.jpg", 'Датский хот-дог': "pictures5/pict6.jpg",
              'Лимонник с сахаром на зиму': "pictures5/pict7.jpeg",
              'Салат из тыквы с яблоком и морковью': "pictures5/pict8.jpg",
              'Салат с консервированными шампиньонами и кукурузой': "pictures5/pict9.jpg",
              'Салат из редьки с морковью с маслом': "pictures5/pict10.jpeg",
              'Салат из редьки с морковью и сметаной': "pictures5/pict11.jpeg",
              'Салат с яблоком, морковью и сыром': "pictures5/pict12.jpeg",
              'Тесто для пиццы на кефире без дрожжей': "pictures5/pict13.jpeg",
              'Салат из вареной свеклы с чесноком': "pictures5/pict14.png",
              'Салат из редьки и моркови с майонезом': "pictures5/pict15.jpg",
              'Кекс без яиц и молока': "pictures5/pict16.jpeg",
              'Печеночный салат с морковью и яйцом': "pictures5/pict17.jpg",
              'Печеночный салат с морковью и огурцом': "pictures5/pict18.jpeg",
              'Салат из свеклы с сыром и чесноком': "pictures5/pict19.jpg",
              'Омлет для детей на сковороде': "pictures5/pict20.jpeg",
              'Кексы без молока и кефира': "pictures5/pict21.jpg",
              'Картофель, запеченный в фольге на углях': "pictures5/pict22.jpg",
              'Салат из капусты со свеклой быстрого приготовления': "pictures5/pict23.jpg",
              'Салат с кальмарами и блинами': "pictures5/pict24.jpg"}

d1_recipes = convert_to_dict(recipes1)  # словарь1 с рецептами
recipe_names1 = list(d1_recipes.keys())  # список1 с названиями блюд
d2_recipes = convert_to_dict(recipes2)  # словарь2 с рецептами
recipe_names2 = list(d2_recipes.keys())  # список2 с названиями блюд
d3_recipes = convert_to_dict(recipes3)  # словарь3 с рецептами
recipe_names3 = list(d3_recipes.keys())  # список3 с названиями блюд
d4_recipes = convert_to_dict(recipes4)  # словарь4 с рецептами
recipe_names4 = list(d4_recipes.keys())  # список4 с названиями блюд
d5_recipes = convert_to_dict(recipes5)  # словарь5 с рецептами
recipe_names5 = list(d5_recipes.keys())  # список5 с названиями блюд

# test()  # перебираем все рецепты

work_bot_fl = True
while work_bot_fl:

    current_date_time = datetime.datetime.now()
    now = current_date_time.time()  # текущее время
    morning = datetime.time(7, 32, 0)  # время начала работы бота
    night = datetime.time(12, 45, 0)  # время окончания работы бота

    if morning < now < night:  # если день
        number_dict = int(*open_text('number_dict.txt'))  # номер словаря
        number_recipe = int(*open_text('number_recipe.txt'))  # номер рецепта

        d_recipes, recipe_names, path_dict = get_path(number_dict)
        # словарь с рецептами, список с названиями блюд, словарь с путями к фото

        print(f"Бот работает, папка с рецептами: {number_dict}, рецепт номер: {number_recipe}")  # проверка бота
        time.sleep(random.randint(60, 7200))  # c 7 до 9 самое популярное время для постов
        promo = random.choice(prom_list)  # реклама
        recipe_name = recipe_names[number_recipe]  # название блюда
        answer = d_recipes[recipe_name]  # выбираем рецепт из словаря по названию блюда

        if len(answer + '\n\n' + promo) < 1000:  # если длиннее, то картинка не прикрепится, ограничение телеграмм
            answer += '\n\n' + promo
        try:
            try:  # этот блок не прерывает работу программы
                files = open(path_dict[recipe_name], 'rb')  # открываем картинку
                bot.send_photo(CHANNEL_NAME, photo=files, caption=answer)  # посылаем ее и рецепт
            finally:
                files.close()  # и закрывает открытый файл если он не прочитался
        except FileNotFoundError:
            print("Невозможно открыть файл с изображением")
        except:
            print("Ошибка при работе с изображением")

        try:  # перебираем рецепты
            if number_recipe < len(recipe_names) - 1:
                # [0,1,2,3] len ==4 => 2 - предпоследний номер и может быть еще увеличен
                number_recipe += 1
            else:
                number_recipe = 0
                number_dict += 1
                try:  # этот блок переключает словарь
                    file = open("number_dict.txt", "w")  # открываем НЕ писать кодировку?
                    file.write(f"{number_dict}")
                finally:
                    file.close()  # и закрывает открытый файл если он не прочитался
            try:  # этот блок переключает рецепт
                file = open("number_recipe.txt", "w")  # открываем НЕ писать кодировку?
                file.write(f"{number_recipe}")
            finally:
                file.close()  # и закрывает открытый файл если он не прочитался
        except FileNotFoundError:
            print("Невозможно открыть файл с номером")
        except:
            print("Ошибка при работе с файлом с номером")

        # таймер работы бота (от 1 до 5 часов)
        time.sleep(random.randint(3600, 17000))  # один-два поста в день достаточно для дзен
