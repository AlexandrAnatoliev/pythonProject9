# pythonProject 9

# БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С РЕЦЕПТАМИ
# Бот получает список рецептов из файла, создает словарь и случайный рецепт (с рекламой!!!) и с фото блюда
# через случайные период времени постит в канал.
# Для этого нам нужно создать свой канал в Telegram,
# добавить в подписчики канала нашего бота и назначить его администратором канала с правом публиковать сообщения.
# Файл с рецептами должен лежать в папке data рядом со скриптом бота.

# $ pip install schedule - установить внешние зависимости

import telebot
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
        recipes1 = f.read().split('\n\n\n')
    finally:
        f.close()

except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлами")

print(recipes1)

# создаем словарь
d_recipes = {}
for recipe in recipes1:
    d_recipes[recipe[:recipe.index("\n\n")]] = recipe

print(d_recipes['Фриттaтa c xлeбoм'])