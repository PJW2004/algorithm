# 함수이름이 단수/복수가 어긋남
# def parse_tokens(token: str, left: int = 1, right: int = 100):
# 타입 힌트의 절반만 채워짐
def parse_token(token: str, left: int = 1, right: int = 100) -> int:
    try:
        value = int(token)
    except ValueError as e:
        # 안쓰는 예외 변수
        # raise ValueError(f"정수를 입력하세요. 입력: {token}")
        # 트레이스백 체인이 유지됨
        # raise ValueError(f"정수를 입력하세요. 입력: {token}") from e
        # 경계가 보이는 형태로 문자 확인
        raise ValueError(f"정수를 입력하세요. 입력: {token!r}") from e
    if not left<=value<=right:
        # 에러 메시지가 매개변수화를 무시함
        # raise ValueError(f"1-100 제한조건에 부합하지 않습니다. 입력: {value}")
        # 트레이스백 간결 (PEP 657)
        raise ValueError(f"{left}-{right} 범위를 벗어났습니다. 입력: {value}") from None
    return value

# 첫번째 줄 공백 사이
tokens = input().split()
if len(tokens) != 2:
    raise ValueError(f"두 정수를 입력하세요. {tokens}")

# 언패킹의 우회로
a, b = map(parse_token, tokens)
# a,b=list(values)

# 여섯 줄의 PRINT는 반복의 리듬이 너무 눈에 띔
# print(int(a>=b))
# print(int(a>b))
# print(int(a<=b))
# print(int(a<b))
# print(int(a==b))
# print(int(a!=b))
# 한번에
results = [a >= b, a > b, a <= b, a < b, a == b, a != b]
print(*map(int, results), sep="\n")