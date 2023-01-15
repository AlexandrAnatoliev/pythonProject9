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
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлами")


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


# def convert_ru_en_chars(word):
#    d_ru_en = {'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'yo', 'ж':'zh', 'з':'z', 'и':'i', 'й':'y', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'i', 'ф':'y', 'х':'k', 'ц':'l', 'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', }

d1_recipes = convert_to_dict(recipes1)  # словарь с рецептами
recipe_names = list(d1_recipes.keys())  # названия блюд

answer = d1_recipes[random.choice(recipe_names)]  # выбираем случайный рецепт из словаря
bot.send_message(CHANNEL_NAME, answer)  # посылаем его
files = open("photo.png", 'rb')  # открываем картинку
bot.send_photo(CHANNEL_NAME, photo=files, caption='фото')  # посылаем ее и текст к ней
# time.sleep(random.randint(16200, 32400)) # один-два поста в день достаточно для дзен
