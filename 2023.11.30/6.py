ticket = input()
sum_1 = 0
sum_2 = 0
for num in range(6):
    if num < 3:
        sum_1 += int(ticket[num])
    else:
        sum_2 += int(ticket[num])
if sum_1 == sum_2:
    print('Да')
else:
    print('Нет')
    
# 183534
# Да    
    
# 401367
# Нет


# 258364
# Нет

# 456771
# Да