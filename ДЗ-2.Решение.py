# Имеем словарь cook_book .Нужно написать функцию, которая на вход принимает список
# блюд из cook_book и количество персон для кого мы будем готовить
# get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количества
# для блюда. Например, для такого вызова
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# Обратите внимание, что ингредиенты могут повторяться
cook_book_dict={
'Омлет': [
   {'ingradient_name': 'Яйцо ', 'quantity': ' 2 ', 'measure': ' шт'},
   {'ingradient_name': 'Молоко ','quantity': ' 100 ','measure': ' мл'},
   {'ingradient_name': 'Помидор ','quantity': ' 2 ','measure': ' шт'}
    ],
 'Утка по-пекински': [
    {'ingradient_name': 'Утка ','quantity': ' 1 ','measure': ' шт'},
    {'ingradient_name': 'Вода ','quantity': ' 2 ','measure': ' л'},
    {'ingradient_name': 'Мед ','quantity': ' 3 ','measure': ' ст.л'},
    {'ingradient_name': 'Соевый соус ','quantity': ' 60 ','measure': ' мл'}
    ],
 'Запеченный картофель': [
     {'ingradient_name': 'Картофель ','quantity': ' 1 ','measure': ' кг'},
     {'ingradient_name': 'Яйцо ', 'quantity': ' 5 ', 'measure': ' шт'},  # Проверка. Добавил повторяющийся инградиент
     {'ingradient_name': 'Чеснок ','quantity': ' 3 ','measure': ' зубч'},
     {'ingradient_name': 'Сыр гауда ','quantity': ' 100 ','measure': ' г'}
     ],
 'Фахитос': [
     {'ingradient_name': 'Говядина ','quantity': ' 500 ','measure': ' г'},
     {'ingradient_name': 'Перец сладкий ','quantity': ' 1 ','measure': ' шт'},
     {'ingradient_name': 'Лаваш ', 'quantity': ' 2 ', 'measure': ' шт'},
     {'ingradient_name': 'Винный уксус ','quantity': ' 1 ','measure': ' ст.л'},
     {'ingradient_name': 'Помидор ','quantity': ' 2 ','measure': ' шт'}
     ]
   }

from pprint import pprint

def get_shop_list_by_dishes(dishes_list, person_count=1):
    ingradient_dict_all = {}
    for dish in dishes_list:

        for el in cook_book_dict[dish]:
            #print(el) # {'ingradient_name': 'Картофель ', 'quantity': ' 1 ', 'measure': ' кг'}
                     # {'ingradient_name': 'Чеснок ', 'quantity': ' 3 ', 'measure': ' зубч'}
                     # {'ingradient_name': 'Сыр гауда ', 'quantity': ' 100 ', 'measure': ' г'}

            ingradient_dict = {} # Создаём словарь с инградиентами для текущего блюда
            ingradient_name=el['ingradient_name'] # Запомнили название инградиента
            working_dict={} # Создаём рабочий словарь с единицей измерения и количеством
            working_dict['measure']=el['measure'] # Вписываем в словарь элементы
            quantity= int(el['quantity'])*person_count # Переменная для количества инградиента в виде целого числа
            working_dict['quantity'] = quantity
            ingradient_dict[ingradient_name]= working_dict
            #print(ingradient_dict) # Для 'Запеченный картофель'на 1 персону:
                                   # {'Картофель ': {'measure': ' кг', 'quantity': 1}}
                                   # {'Чеснок ': {'measure': ' зубч', 'quantity': 3}}
                                   # {'Сыр гауда ': {'measure': ' г', 'quantity': 100}}
            # Проверка на повторяющиеся инградиенты
            # Для ключа key из списка ключей словаря ingradient_dict :
            for key in ingradient_dict:
                # Если ключ key уже есть в списке ключей финишного словаря ingradient_dict_all :
                if key in ingradient_dict_all:
                # К значению ключа 'quantity' у текущего словаря ingradient_dict прибавим значение из финишного словаря.

                    ingradient_dict[key]['quantity'] += ingradient_dict_all[key]['quantity']
            # Т.к. функция update() при совпадении ключей перезаписывает совпадающий ключ  ,
            # оставляя значение по вновь добавленному ключу , получаем сумму значений - добавляемого и того,
            # что уже записали ранеее
            ingradient_dict_all.update(ingradient_dict)
    pprint(ingradient_dict_all) # C проверкой на повтроряющийся инградиент

get_shop_list_by_dishes(['Омлет','Запеченный картофель'],2)


