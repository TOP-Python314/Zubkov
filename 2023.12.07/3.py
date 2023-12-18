first_list, second_list  = list(input()), list(input())
result = ''
for i in range(len(second_list)):
    if first_list[i] != second_list[i]:
        result = 'нет'
        break
    elif first_list[i] == second_list[i]:
        result = 'да'
print(result)


# 1 2 3 4
# 1 2
# да


# 1 2 3 4
# 2 4
# нет

# 4 5 6 8 0
# 6 3 5
# нет

# 4 5 6 7 8 9 0
# 4 5 6
# да