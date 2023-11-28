number_1, number_2, number_3 = float(input()), float(input()), float(input())
total = 0
if number_1 > 0:
    total += number_1
if number_2 > 0:
    total += number_2
if number_3 > 0:
    total += number_3
if total.is_integer():
    print(f"{total:.0f}")
else:
    print(total) 
    
    
    
# 1.34
# -3.9
# 7
# 8.34


# 7
# -15
# 7
# 14

# 90
# -20.34
# 5.8
# 95.8
    