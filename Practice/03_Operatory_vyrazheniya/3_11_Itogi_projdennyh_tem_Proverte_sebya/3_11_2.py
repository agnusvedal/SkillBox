""" Задача 2. Поменять местами
Вы уже умеете менять местами строковые переменные и знаете, что в них также можно хранить числа.
Напишите программу, которая меняет значения двух переменных местами. Использовать третью переменную и «синтаксический сахар» (конструкция a, b = b, a) нельзя. В переменные будут вводиться только числа.
Скопируйте этот код и вставьте в редактор Replit, чтобы решить задачу. Не меняйте уже написанный код (input и print).
Можете вставить между принтами любое количество строк кода, которое вам нужно для решения.
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
# Здесь вы можете написать любое количество строк кода. Менять, удалять, переставлять строки выше и ниже — нельзя.
print(a, b) """

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
#3,5
a = a + b
b = a - b
a = a - b

print(a, b)
