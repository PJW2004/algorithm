def parse_tokens(token: str, left: int = 1, right: int = 100):
    try:
        value = int(token)
    except ValueError as e:
        raise ValueError(f"정수를 입력하세요. 입력: {token}")
    if not left<=value<=right:
        raise ValueError(f"1-100 제한조건에 부합하지 않습니다. 입력: {value}")
    return value

# 첫번째 줄 공백 사이
tokens = input().split()
if len(tokens) != 2:
    raise ValueError(f"두 정수를 입력하세요. {tokens}")
values = map(parse_tokens, tokens)
a,b=list(values)
print(int(a>=b))
print(int(a>b))
print(int(a<=b))
print(int(a<b))
print(int(a==b))
print(int(a!=b))