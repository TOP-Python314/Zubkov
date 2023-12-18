scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}
word = input().upper()
total = []
for i in word:
    for key, value in scores_letters.items():
        if value.count(i) > 0:
            total.append(key)
            break
print(sum(total))    



# синхрофазотрон
# 29