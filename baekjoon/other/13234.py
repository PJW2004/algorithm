value1,operation,value2=input().split()
replace_type = lambda string: True if string == "true" else False
if operation=="AND":
    print(str(replace_type(value1) and replace_type(value2)).lower())
else:
    print(str(replace_type(value1) or replace_type(value2)).lower())