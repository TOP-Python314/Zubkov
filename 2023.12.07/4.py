dict_base = {}
while True:
    list_name_error = input().split()
    if len(list_name_error) == 0:
        break
    else:
        dict_base.update({list_name_error[0]: list_name_error[1]})

value = input()
code = 0 
for key, val in dict_base.items():
    if val == value:
        code = int(key)  
print(code if code > 1 else '! value error !')



# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB
# 1007 ER_DB_CREATE_EXISTS
# 1008 ER_DB_DROP_EXISTS
# 1010 ER_DB_DROP_RMDIR
# 1016 ER_CANT_OPEN_FILE
# 1022 ER_DUP_KEY

# ER_DUP_KE
# ! value error !



# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB
# 1007 ER_DB_CREATE_EXISTS
# 1008 ER_DB_DROP_EXISTS
# 1010 ER_DB_DROP_RMDIR
# 1016 ER_CANT_OPEN_FILE
# 1022 ER_DUP_KEY

# ER_CANT_CREATE_FILE
# 1004


# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB
# 1007 ER_DB_CREATE_EXISTS
# 1008 ER_DB_DROP_EXISTS
# 1010 ER_DB_DROP_RMDIR
# 1016 ER_CANT_OPEN_FILE
# 1022 ER_DUP_KEY

# ER_DUP_KEY
# 1022