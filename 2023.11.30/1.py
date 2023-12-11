number_list =[]
while True:
    num = int(input())
    if num % 7 == 0:
        number_list.append(num)
    else:
        break
number_list.reverse()  
print(*number_list)



# 7
# 70
# 54
# 70 7


# 7
# 7
# 14
# 21
# 13
# 21 14 7 7