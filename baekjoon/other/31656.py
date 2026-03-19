raw_message=input()
temp_message=""
result_message=""
for message in raw_message:
    if message == temp_message:
        continue
    temp_message=message
    result_message+=message
print(result_message)