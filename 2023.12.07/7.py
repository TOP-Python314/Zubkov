list_of_dicts = [
    {
        'Барнаул': 7,
        'Владивосток': 9,
        'Волгоград': 9,
        'Ижевск': 5,
        'Махачкала': 7,
        'Москва': 9,
        'Омск': 9,
        'Саратов': 4,
        'Ульяновск': 3
    },
    {
        'Казань': 8,
        'Краснодар': 2,
        'Москва': 3,
        'Самара': 3,
        'Санкт-Петербург': 6,
        'Тюмень': 1,
        'Уфа': 7
    },
    {
        'Ижевск': 1,
        'Иркутск': 3,
        'Кемерово': 1,
        'Москва': 3,
        'Саратов': 3,
        'Хабаровск': 6
    },
    {
        'Барнаул': 7,
        'Оренбург': 3,
        'Санкт-Петербург': 1,
        'Тюмень': 4,
        'Ярославль': 3
    }
]

result = dict()
for elem in list_of_dicts:
    for key, value in elem.items():
        if result.get(key) == None:
            result[key] = set()
        if value != result.get(key):
            result[key].add(value)
all_dict = dict(sorted(result.items()))            

for key in all_dict:
    print(key, result[key])         


# Барнаул {7}
# Владивосток {9}
# Волгоград {9}
# Ижевск {1, 5}
# Иркутск {3}
# Казань {8}
# Кемерово {1}
# Краснодар {2}
# Махачкала {7}
# Москва {9, 3}
# Омск {9}
# Оренбург {3}
# Самара {3}
# Санкт-Петербург {1, 6}
# Саратов {3, 4}
# Тюмень {1, 4}
# Ульяновск {3}
# Уфа {7}
# Хабаровск {6}
# Ярославль {3}
     
        
        
    