name_file = input()
name_cler = [elem.rstrip(';')for elem in name_file.split()]
dict_name_file = {name: name_cler.count(name) for name in set(name_cler)}
new_name_file = []
for name, coun in dict_name_file.items():
    if coun > 1:
        index_dot = name.find('.')
        for i in range(1, coun + 1):
            if i == 1:
                new_name_file.append(name)
            else:  
                new_name_file.append(f'{name[:index_dot]}_{i}{name[index_dot:]}') 
    else:
        new_name_file.append(name)
for super_name_file in new_name_file:
    print(super_name_file)    
    
    
    
    
# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz



# functions.h
# aux.h
# src.tar.gz
# src_2.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# main.cpp
# main_2.cpp
# main_3.cpp


# 1.py; 1.py; 1.py; aux.h; functions.h; main.cpp; main.cpp;  main.py; src.tar.gz; src.tar.gz



# main.py
# src.tar.gz
# src_2.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# main.cpp
# main_2.cpp
# functions.h
# aux.h