# -> 32ms 걸림
# 6 글자씩 자르면 될거 같고.
# 유사도가 가장 높은 데이터를 전달하면 될 것으로 판단됨.
# 두 자 이상이 다르면 이런 것이 처음 나오는 문자의 위치를 전달하고 끝.
items = {
    "A": "000000",
    "B": "001111",
    "C": "010011",
    "D": "011100",
    "E": "100110",
    "F": "101001",
    "G": "110101",
    "H": "111010"
}

_ = int(input())
character_data = input()
chunk_size = 6
output = ""
for index, chunk in enumerate(range(0, len(character_data), chunk_size)):
    chunking:str = character_data[chunk:chunk+chunk_size]

    # 글자에 대한 유사도 측정 필요.
    lanking_items = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0
    }
    check = False
    for key, value in items.items():
        for chunking_data, chunking_value in zip(chunking, value):
            if chunking_data == chunking_value:
                lanking_items[key] += 1
        if lanking_items[key] == 6:
            output += key
            check = True
            break
    if check:
        continue
    
    lanking_items = [(value, key) for key, value in lanking_items.items()]
    lanking_items.sort(reverse=True)
    if lanking_items[0][0] < 5:
        print(index+1)
        exit()
    output += lanking_items[0][1]
if output:
    print(output)