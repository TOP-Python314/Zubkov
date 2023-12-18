fruti = [] 
while True:
    elem = input()
    if elem == '':
        break
    else: 
        fruti.append(elem)

if len(fruti) == 1:
    print(*fruti)
else:
    print(f'{", ".join(fruti[:-1])} и {fruti[-1]}')




# яблоко

# яблоко



# яблоко
# груша

# яблоко и груша



# яблоко
# груша
# апельсин

# яблоко, груша и апельсин



# яблоко
# груша
# апельсин
# лимон

# яблоко, груша, апельсин и лимон