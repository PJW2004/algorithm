n = int(input())
if not -100<=n<=100:
    raise ValueError(f"제한조건 범위에 해당하지 않습니다. 입력: {n}")
print(n)
if n < 0:
    print("minus")