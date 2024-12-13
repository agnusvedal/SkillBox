# Поменять местами содержимое стакана и кружки (glass, mug)

glass = input('Введите значение стакана: ')
mug = input('Введите значение кружки: ')
print('Обмен содержимым:')

# основной длинный вариант
switch = glass
glass = mug
mug = switch

# альтернативный профессиональный вариант
#glass, mug = mug, glass

print('В стакане: ', glass)
print('В кружке: ', mug)
