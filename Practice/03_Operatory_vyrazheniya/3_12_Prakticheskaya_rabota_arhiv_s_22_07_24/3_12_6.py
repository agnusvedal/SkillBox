""" Задача 6. Проверяем бухгалтера
Невнимательный бухгалтер Антон складывает числа быстро, но иногда забывает о двух последних разрядах. Чтобы помочь Антону, напишите программу, которая бы складывала только два последних разряда. 
Реализуйте программу, которая запрашивает два числа у пользователя. После этого у каждого числа возьмите две последние цифры. Получившиеся два числа сложите и выведите на экран. """

num_one = int(input('Введите первое число: '))
num_two = int(input('Введите второе число: '))
sum = num_one % 100 + num_two % 100
print('Сумма:', sum)
