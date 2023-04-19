import os
from pprint import pprint
# В переменной folder_path запомнили путь к папке , содержащей все наши текстовые файлы :
folder_path = r'D:\PYTHON\НЕТОЛОГИЯ\Обучающие проекты - НЕТОЛОГИЯ\Лекция 10 . Открытие и чтение файла, запись в файл\Домашнее задание по теме- Открытие и чтение файла , запись в файл\ДЗ-3. Текстовые файлы'
# В переменную my_files запишем названия наших файлов используя функцию listdir() библиотеки os ,
# которая возвращает названия файлов , считывая их по месту расположения на компьютере (folder_path ):
my_files = os.listdir(folder_path)
#print(my_files) #['1.txt', '2.txt', '3.txt']
# создаем пустой список для загрузки данных из файлов
common_txt_file_list = []
#делаем цикл по списку имен файлов
for file_name in my_files:
    with open(f'{folder_path}\{file_name}', 'r', encoding="utf8") as f:
        # Записываем в переменную file_lines содержимое текущего файла (сам текст):
        file_lines = f.readlines()
        #print(file_lines)
        # добавляем в общий список данные по текущему файлу - длину текущего файла (len(file_lines) ,
        # название файла - file_name  и список со строками текущего текста . Получим список со скписками внутри.
        common_txt_file_list.append([str(len(file_lines)), file_name, file_lines])
#  Произведём сортировку полученного списка common_txt_file_list по количеству строк в файлах ( от меньшего к большему)
common_txt_file_list.sort()
pprint(common_txt_file_list)
# Запишем данные из полученного списка в новый файл finish.txt методом дозаписи "а" :
with open('finish.txt','a',encoding="utf8") as f:
    for list_ in common_txt_file_list:
        for el in list_:
            f.writelines(el)
            f.write('\n') # Записали разделитель строк
        f.write('\n') # Разделитель блоков ( для удобства )
# Результат записан в finish.txt