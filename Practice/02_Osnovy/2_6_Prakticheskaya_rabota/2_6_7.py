""" Задача 7. Путь к файлу
Что нужно сделать
К каждому файлу на компьютере можно узнать путь. Выглядит он примерно так:
'C:/user/docs/folder/new_file.txt'
Напишите программу, которая запрашивает у пользователя его имя и имя файла (переменные user и new_file соответственно). Используя операцию конкатенации, выведите путь к файлу на экран """


user = input('Введите имя пользователя латиницей: ')
new_file = input('Введите имя файла: ')
print('Путь к файлу:' , 'C:/' + user + '/docs/folder/' + new_file + '.txt')
