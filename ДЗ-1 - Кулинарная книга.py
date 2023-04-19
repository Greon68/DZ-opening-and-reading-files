# Необходимо написать программу для кулинарной книги

# Инградиенты - в Culinary_recipes.txt
from pprint import pprint

with open('Culinary_recipes.txt', 'rt',encoding='utf-8') as file:
    cook_book= {} # Создали пустой словарь
    for line in file:
        dish=line.strip() # Считали и сохранили название блюда
        number_ingradients = int(file.readline().strip()) # количество инградиентов в блюде
        ingradients_list=[] # Список инградиентов для текущего блюда
        for _ in range(number_ingradients) :
            # Считываем построчно информацию об инградиентах блюда
            ingredient_name,quantity,measure= file.readline().strip().split('|')
            # Сохраняем информацию об инградиентах текущего блюда в список ingradients_list в виде словаря
            ingradients_list.append({
             'ingradient_name': ingredient_name,
             'quantity':quantity ,
             'measure': measure })
        file.readline() # Считали пустую строку без записи
        cook_book[dish]=ingradients_list # Создали элемент словаря , где ключ - название блюда ,
                                           # а значение - список инградиентов
    pprint(cook_book , sort_dicts=False)

# Результат :
# {'Омлет': [
#    {'ingradient_name': 'Яйцо ', 'quantity': ' 2 ', 'measure': ' шт'},
#    {'ingradient_name': 'Молоко ','quantity': ' 100 ','measure': ' мл'},
#    {'ingradient_name': 'Помидор ','quantity': ' 2 ','measure': ' шт'}
#     ],
#  'Утка по-пекински': [
#     {'ingradient_name': 'Утка ','quantity': ' 1 ','measure': ' шт'},
#     {'ingradient_name': 'Вода ','quantity': ' 2 ','measure': ' л'},
#     {'ingradient_name': 'Мед ','quantity': ' 3 ','measure': ' ст.л'},
#     {'ingradient_name': 'Соевый соус ','quantity': ' 60 ','measure': ' мл'}
#     ],
#  'Запеченный картофель': [
#      {'ingradient_name': 'Картофель ','quantity': ' 1 ','measure': ' кг'},
#      {'ingradient_name': 'Чеснок ','quantity': ' 3 ','measure': ' зубч'},
#      {'ingradient_name': 'Сыр гауда ','quantity': ' 100 ','measure': ' г'}
#      ],
#  'Фахитос': [
#      {'ingradient_name': 'Говядина ','quantity': ' 500 ','measure': ' г'},
#      {'ingradient_name': 'Перец сладкий ','quantity': ' 1 ','measure': ' шт'},
#      {'ingradient_name': 'Лаваш ', 'quantity': ' 2 ', 'measure': ' шт'},
#      {'ingradient_name': 'Винный уксус ','quantity': ' 1 ','measure': ' ст.л'},
#      {'ingradient_name': 'Помидор ','quantity': ' 2 ','measure': ' шт'}
#      ]
#    }


































