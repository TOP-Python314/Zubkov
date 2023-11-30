option_1, option_2 = input(), input()
letter_1 = option_1[0]
letter_2 = option_2[0]
number_1 = int(option_1[1])
number_2 = int(option_2[1])
cell_1 = ''
cell_2 = ''

if letter_1 in 'aceg' and number_1 % 2 != 0:
    cell_1 = 'black'
elif letter_1 in 'bdfh' and number_1 % 2 == 0:
    cell_1 = 'black'
    
if letter_2 in 'aceg' and number_2 % 2 != 0:
    cell_2 = 'black'
elif letter_2 in 'bdfh' and number_2 % 2 == 0:
    cell_2 = 'black'
    
if letter_1 > 'h' or letter_2 > 'h' or number_1 > 8 or number_2 > 8:
    print('не корректный ввод')   
elif cell_1 == cell_2:
    print('да')
else: 
    print('нет')


# a3
# b5
# нет


# v6
# a2
# не корректный ввод

# a1
# b2
# да