"""
정수 n 이 주어짐.
정수 n 의 제한 조건은 -200~200임.
"""
token:str = input()
try:
    n = int(token)
except ValueError:
    # raise ValueError(f"정수를 입력해 주세요. 입력: {token!r}")
    # 깜빡
    raise ValueError(f"정수를 입력해 주세요. 입력: {token!r}") from None

if not -200<=n<=200:
    raise ValueError(f"제한 조건(-200~200)에 부합하지 않습니다. 입력: {n}")

if n<0:
    print("ice")
elif 100<=n:
    print("vapor")
else:
    print("water")