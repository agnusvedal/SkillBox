""" Вы разрабатываете программу для умных часов. В переменной minutes задаётся некоторое количество минут. Напишите программу, которая преобразует указанное количество минут в часы и минуты, и выведите результат на экран. """

minutes = 200
hours = minutes // 60
rest_minutes = minutes % 60
print(minutes, 'минут — это', hours, 'ч. и', rest_minutes, 'мин.')
