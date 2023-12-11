number = int(input())
subs = [1, 1]
if number == 1:
    print(1)
else:
    for num in range(number - 2):
        sum_ = subs[num] + subs[num + 1]
        subs.append(sum_)
    print(*subs)
    
    
    
# 6
# 1 1 2 3 5 8


# 1
# 1


# 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

# 13
# 1 1 2 3 5 8 13 21 34 55 89 144 233