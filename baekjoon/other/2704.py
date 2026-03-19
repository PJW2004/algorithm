def get_binary(number:int):
    binary = ""
    # 2**5, 2**4, 2**3, 2**2, 2**1, 2**0
    for square in range(5, 0, -1):
        if number - 2**square >= 0:
            number -= 2**square
            binary += "1"
        else:
            binary += "0"
    return binary + str(number)

for _ in range(int(input())):
    hour_binary,minute_binary,second_binary=map(get_binary, map(int, input().split(':')))

    # 10시 37분 49초
    # 3열 방식 : 011001100010100011
    three_row = ""
    for hour_binary_chunk, minute_binary_chunk, second_binary_chunk in zip(hour_binary, minute_binary, second_binary):
        three_row += hour_binary_chunk + minute_binary_chunk + second_binary_chunk
    
    # 3행 방식 : 001010100101110001
    three_column = hour_binary + minute_binary + second_binary
    print(f"{three_row} {three_column}")