number_1, number_2 = int(input()), int(input())
if number_1 % number_2 == 0:
    print(
        f'{number_1} делиться  на {number_2}',
        f'частное: {number_1 / number_2:.0f}',
        sep='\n'
)
else:
    print(
        f'{number_1} не делится на {number_2} нацело',
        f'не полное частное: {number_1 // number_2}',
        f'остаток: {number_1 % number_2}',
        sep='\n'
)     


# 8
# 2
# 8 делиться  на 2
# частное: 4

# 10
# 3
# 10 не делится на 3 нацело
# не полное частное: 3
# остаток: 1

# 1000
# 52
# 1000 не делится на 52 нацело
# не полное частное: 19
# остаток: 12