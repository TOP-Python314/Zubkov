number = int(input())
total = [number + 1]

for div in range(2, number // 2 + 1):
    if number % div == 0:
        total.append(div)
print(sum(total))
    
    
# 50
# 93


# 65
# 84

# 61
# 62