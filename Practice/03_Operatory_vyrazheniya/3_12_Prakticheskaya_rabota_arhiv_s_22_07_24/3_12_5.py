""" Задача 5. Часы
Напишите программу, которая получает на вход число n (количество минут), затем считает, сколько это будет в часах и сколько минут останется, и выводит на экран эти два результата."""

minutes =int(input('Введите количество минут: '))
hours = minutes // 60
rem_minutes = minutes % 60

print('Введено', hours, 'часов и', rem_minutes, 'минут')
