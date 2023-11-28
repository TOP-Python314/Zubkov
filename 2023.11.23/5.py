option_1, option_2 = input(), input()
letter_1 = option_1[0]
letter_2 = option_2[0]
number_1 = int(option_1[1])
number_2 = int(option_2[1])

if letter_1 == letter_2 and number_1 != number_2 or letter_1 != letter_2 and number_1 == number_2:
    print('да')
else:
    print('нет')

# b6
# h8
# нет

# c4
# b6
# нет

# a1
# a5
# да

# a3
# c3
# да
