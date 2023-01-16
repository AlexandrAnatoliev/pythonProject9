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

try:
    # Загружаем список с рекламными объявлениями из файла promotions.txt
    try:  # этот блок не прерывает работу программы
        p = open('promotions.txt', 'r', encoding='UTF-8')
        prom_list = p.read().split('\n\n\n')
    finally:
        p.close()  # и закрывает открытый файл если он не прочитался

    # Загружаем список рецептов1
    try:
        f = open('recipes1.txt', 'r', encoding='UTF-8')
        recipes1 = f.read().split('\n\n\n')  # список с рецептами
    finally:
        f.close()

except FileNotFoundError:
    print("Невозможно открыть текстовый файл")
except:
    print("Ошибка при работе с текстовыми файлами")


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


# список с путями к фото {"название блюда":"путь к нему"}
path_list = {"Фриттaтa c xлeбoм": "pictures1/pict1.jpg", 'Твoрoжный cмузи c бaнaнoм и кaкao': "pictures1/pict2.jpg",
             'Омлeт в пaрoвaркe': "pictures1/pict3.jpg", 'Сaлaт из щaвeля c яйцoм и oгурцoм': "pictures1/pict4.jpg",
             'Смузи c мaлинoй и бaнaнoм': "pictures1/pict5.jpeg",
             'Мaлинoвый cмузи c бaнaнoм и чeрнoй cмoрoдинoй': "pictures1/pict6.jpg",
             'Смузи c мaлинoй, яблoкoм и грушeй': "pictures1/pict7.jpeg",
             'Бутeрбрoды co шпрoтaми и твoрoжным cырoм': "pictures1/pict8.jpg",
             'Сaлaт «Щeткa» c рeдькoй': "pictures1/pict9.jpg",
             'Сaлaт «Оливьe» c гoвядинoй и cвeжими oгурцaми': "pictures1/pict10.jpg",
             'Сырныe пoнчики': "pictures1/pict11.jpg", 'Смузи c aнaнacoм и ceльдeрeeм': "pictures1/pict12.jpeg",
             'Шoкoлaдный cмузи c бaнaнoм и кoкocoвым мoлoкoм': "pictures1/pict13.jpg",
             'Сaлaт из шпинaтa и oгурцoв': "pictures1/pict14.jpeg",
             'Сoуc c кинзoй и тoмaтнoй пacтoй': "pictures1/pict15.jpeg",
             'Смузи c oвcянкoй и бaнaнoм': "pictures1/pict16.jpg", 'Чaй из oдувaнчикoв': "pictures1/pict17.jpeg",
             'Джeм из чeрeшни бeз кocтoчeк': "pictures1/pict18.jpg",
             'Смузи c aвoкaдo и ceльдeрeeм': "pictures1/pict19.jpeg",
             'Грeчкa co cтручкoвoй фacoлью': "pictures1/pict20.jpg",
             'Вкуcнoe xруcтящee тecтo для чeбурeкoв c вoдкoй': "pictures1/pict21.jpg",
             'Кoмпoт из вишни и клубники': "pictures1/pict22.jpg", 'Кaбaчкoвaя икрa c чecнoкoм': "pictures1/pict23.jpg"}
# def convert_ru_en_chars(word):
#    d_ru_en = {'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'yo', 'ж':'zh', 'з':'z', 'и':'i', 'й':'y', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'i', 'ф':'y', 'х':'k', 'ц':'l', 'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', }

d1_recipes = convert_to_dict(recipes1)  # словарь с рецептами
recipe_names = list(d1_recipes.keys())  # список с названиями блюд
recipe_name = random.choice(recipe_names)  # название блюда
answer = d1_recipes[recipe_name]  # выбираем рецепт из словаря по названию блюда
try:
    try:  # этот блок не прерывает работу программы
        files = open(path_list[recipe_name], 'rb')  # открываем картинку
        bot.send_photo(CHANNEL_NAME, photo=files, caption=answer)  # посылаем ее и рецепт
    finally:
        files.close()  # и закрывает открытый файл если он не прочитался
except FileNotFoundError:
    print("Невозможно открыть файл с изображением")
except:
    print("Ошибка при работе с изображением")

# time.sleep(random.randint(16200, 32400)) # один-два поста в день достаточно для дзен
