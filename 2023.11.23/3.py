year = int(input())
if year % 4 == 0 and year % 100 or year % 400 == 0:
    print('да') 
else:
   print('нет')
   
# 3030
# нет

# 2020
# да
