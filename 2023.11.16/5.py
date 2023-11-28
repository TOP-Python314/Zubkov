integer = input()
fraction = input()

# ИСПОЛЬЗОВАТЬ везде: круглые скобки используются для литерала кортежа, изменения порядка вычисления выражений, вызова функций и записи составного выражения на нескольких строчках — больше нигде и никак
# вот такой вариант, тоже рабочий
result = float(integer + '.' + fraction)

# КОММЕНТАРИЙ: ваш вариант вполне корректный и рабочий, но количество операций избыточно: конкатенация, два преобразования, сложение
# ИСПОЛЬЗОВАТЬ: всё это можно заменить куда более простым выражением:
result = float(f'{integer}.{fraction}')

print(f'{result} миль = {result*1.61:.1f}')


# 15
# 7
# 15.7 миль = 25.3

# 10
# 25
# 10.25 миль = 16.5

# 23
# 234
# 23.234 миль = 37.4


# ИТОГ: хорошо — 4/5
