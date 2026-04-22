"""정수 n원으로 살 수 있는 가장 비싼 물건의 이름을 출력.

가격표:
    book: 3000원
    mask: 1000원
아무것도 살 수 없으면 'no' 출력.
"""
token = input()
try:
    n = int(token)
except ValueError:
    raise ValueError(f"정수가 아닙니다. 입력: {token!r}") from None

if not 0<=n<=10_000:
    raise ValueError(f"제한조건(1~10,000)에 부합하지 않습니다. 입력: {n}")

# 코드차이
ITEMS = [("book", 3_000), ("mask", 1_000)]

for name, price in sorted(ITEMS, key=lambda x: x[1], reverse=True):
    if n >= price:
        print(name)
        break
else:
    print("no")
