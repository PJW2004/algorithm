def convert_base(number, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if number < base:
        return digits[number]
    else:
        return convert_base(number // base, base) + digits[number % base]
    
number, base = map(int, input().split())
temp = ""
temp_list = []
binary_data = convert_base(number, base)
for index, text in enumerate(binary_data):
    if text == "0":
        if temp:
            temp_list.append(int(temp))
            temp = ""
    else:
        temp += text
        if index == len(binary_data) -1:
            temp_list.append(int(temp))    
print(convert_base(sum(temp_list), base))