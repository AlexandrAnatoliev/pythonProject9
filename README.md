# pythonProject9

[Ru] БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С РЕЦЕПТАМИ

## Описание

#### Бот получает список рецептов из файла, создает словарь и случайный рецепт (с рекламой!!!) и с фото блюда через случайные период времени постит в канал.

## Требования

* Установить внешние зависимости
* $ pip install -r requirements.txt
* Создать свой канал в Telegram, добавить в подписчики канала нашего бота и назначить его администратором канала с
  правом публиковать сообщения.
* Создать файлы с рецептами (recipes1.txt, recipes2.txt...) и размесить в папке со скриптом бота.
* Создать папки с фото блюд (pictures1, pictures2...)
* Создать файл promotions.txt со списком реклам
* Создать файл config.py, в котором будут храниться токен для доступа к боту и адрес телеграм-канала (начинается с @) в
  виде

```python
token = "1234567890:ASDFGHH..."
channel = '@topjokes...'
```

## Где взять токен?

* https://xakep.ru/2021/11/28/python-telegram-bots/

## Подключаем модули

```python
import telebot
import random
import time
import datetime
from config import token, channel
```

## Примеры использования

#### Загружаем список рекламы и рецептов

Указываем название текстового файла с рецептами, 'r' - чтение текста, кодировку текта 'UTF-8'
Рецепты в текстовом файле разделены двумя пустыми строками (\n\n\n)

```python
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
```

#### Обработка исключений

Закрывает открытый файл, если он не прочитался

```python
# Загружаем список с рекламными объявлениями из файла promotions.txt
try:  # этот блок не прерывает работу программы 
    p = open('promotions.txt', 'r', encoding='UTF-8')
    prom_list = p.read().split('\n\n\n')
finally:
    p.close()  # и закрывает открытый файл если он не прочитался
```

Этот блок прерывает работу программы и пишет причину

```python
try:
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлами")
```

#### Для удобства работы преобразуем списоки с рецептами в словари

```python
def convert_to_dict(recipe_list):
    d_recipes = {}
    for recipe in recipe_list:
        d_recipes[recipe[:recipe.index("\n\n")]] = recipe
    return d_recipes
```

#### Тестовая функция

Перебирает все блюда. Стабильно обрабатывает 10-20 сообщений (использовать срезы списков). Выводит название блюда и
длину сообщения

```python
def test():
    for recipe_name in recipe_names2[10:]:  # Перебирем все блюда. Если выводит ошибку - попрововать сделать срез списка
        time.sleep(2)
        promo = random.choice(prom_list)  # реклама
        print(f"recipe_name: {recipe_name}, promo: {promo}")
        answer = d2_recipes[recipe_name]  # выбираем рецепт из словаря по названию блюда
        if len(answer + '\n\n' + promo) < 1000:
            answer += '\n\n' + promo

        print("длина рецепта: ", len(answer))  # если длина более 1024, то картинку не закрепить
        try:
            try:  # этот блок не прерывает работу программы
                files = open(path_dict2[recipe_name], 'rb')  # открываем картинку
                bot.send_photo(CHANNEL_NAME, photo=files, caption=answer)  # посылаем ее и рецепт
            finally:
                files.close()  # и закрывает открытый файл если он не прочитался
        except FileNotFoundError:
            print("Невозможно открыть файл с изображением")
        except:
            print("Ошибка при работе с изображением")
```

#### Определяет случайным образом из какой папки будут браться рецепты. Возвращает: словарь с рецептами, список с названиями блюд, словарь с путями к фото

```python
def get_path():
    ind = random.randint(1, 2)
    if ind == 1:
        d_rec = d1_recipes
        recipe_n = recipe_names1
        path_d = path_dict1
    else:
        d_rec = d2_recipes
        recipe_n = recipe_names2
        path_d = path_dict2
    return d_rec, recipe_n, path_d
```

#### Cписок1 с путями к фото {"название блюда":"путь к нему"}

```python
path_dict1 = {"Фриттaтa c xлeбoм": "pictures1/pict1.jpg", 'Твoрoжный cмузи c бaнaнoм и кaкao': "pictures1/pict2.jpg"}
```

#### Выставляем время начала работы бота "morning" и окончания "night", чтобы сообщения не будили по ночам

```python
work_bot_fl = True
while work_bot_fl:
    current_date_time = datetime.datetime.now()
    now = current_date_time.time()  # текущее время
    morning = datetime.time(7, 3, 0)  # время начала работы бота
    night = datetime.time(18, 45, 0)  # время окончания работы бота
```

#### Посылаются случайные рецепты через случайные периоды времени в диапазоне от 1  до 5 часов

```python
    if morning < now < night:  # если день
    print("Бот работает (день)")  # проверка бота
    d_recipes, recipe_names, path_dict = get_path()  # словарь с рецептами, список с названиями блюд, словарь с путями к фото
    time.sleep(random.randint(60, 7200))  # c 7 до 9 самое популярное время для постов
    promo = random.choice(prom_list)  # реклама
    recipe_name = random.choice(recipe_names)  # название блюда - случайное
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
    # таймер работы бота (от 1 до 5 часов)
    time.sleep(random.randint(16200, 32400))  # один-два поста в день достаточно для дзен
```
