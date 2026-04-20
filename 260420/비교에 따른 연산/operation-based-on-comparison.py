# 공백을 두고 주어짐.
tokens:list = input().split()
if len(tokens) != 2:
    # 두 값이 주어짐.
    raise ValueError(f"두 정수를 공백을 두고 입력하세요. 개수: {len(tokens)}") from None

def bounded_token(token: str, left: int, right: int) -> int:
    try:
        value = int(token)
    except ValueError as e :
        raise ValueError(f"정수가 아닙니다. 입력: {token!r}") from e
    if not left<=value<=right:
        raise ValueError(f"제한 조건({left}<=value<={right})에 부합하지 않습니다. 입력: {value}") from None
    return value

# 리스트 컨프리헨션
a,b = [bounded_token(token, 1, 100) for token in tokens]

if a>b:
    # a가 b보다 크다면
    # 두수의 곱
    print(a*b)
else:
    # 그렇지 않다면
    # b를 a로 나눈 몫
    print(b//a)