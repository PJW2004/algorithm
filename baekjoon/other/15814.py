charactor = list(input())
for _ in range(int(input())):
    a, b = map(int, input().split())
    temp_a = charactor[a]
    charactor[a] = charactor[b]
    charactor[b] = temp_a
print("".join(charactor))