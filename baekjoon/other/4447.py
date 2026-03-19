# g 가 더 많으면 좋은놈
# b 가 더 많으면 나쁜놈
# g 랑 b 가 같으면 중립
for _ in range(int(input())):
    name = input()
    g_count = name.lower().count('g')
    b_count = name.lower().count('b')
    if g_count == b_count:
        print(f'{name} is NEUTRAL')
    elif g_count > b_count:
        print(f'{name} is GOOD')
    else:
        print(f'{name} is A BADDY')