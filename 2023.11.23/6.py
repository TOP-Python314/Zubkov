option_1, option_2 = input(), input()
letter_1 = ord(option_1[0])
letter_2 = ord(option_2[0])
number_1 = int(option_1[1]) + 96
number_2 = int(option_2[1]) + 96

if letter_1 > 104 or letter_2 > 104 or number_1 > 104 or number_2 > 104:
    print('не корректный ввод')
elif abs(letter_1 - letter_2 > 1) or abs(number_1 - number_2) > 1:
    print('нет')
else:
    print('да')
    
    
# a1
# a3
# нет

# h8
# h7
# да

# i8
# j7
# не корректный ввод

# a2
# b3
# да


