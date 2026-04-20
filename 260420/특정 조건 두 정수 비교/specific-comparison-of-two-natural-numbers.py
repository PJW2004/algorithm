# 공백을 사이에 두고 주어짐
tokens:list = input().split()
if len(tokens) != 2:
    # 두개의
    raise ValueError(f"공백을 사이로 2개만 입력하세요. 입력: {tokens}") from None

def bounded_token(token: str, left: int, right: int) -> int:
    try:
        value = int(token)
    except ValueError as e:
        # 정수를 입력받아.
        raise ValueError(f"정수를 입력해 주세요. 입력: {token!r}") from e
    if not left<=value<=right:
        # 제한조건
        raise ValueError(f"제한조건({left}<=value<={right})에 부합하지 않습니다. 입력: {value}") from None
    return value

# 리스트 컴프리헨션
# 제한 조건 1~100
A,B = [bounded_token(token, 1, 100) for token in tokens]

# 첫 번째 수가 더 작으면
# 두 개의 수가 같으면
check_values = [A < B, A == B]

# 맞으면 1 아니면 0
check_output = map(int, check_values)

# 결과값 두 개를 공백을 사이에 두고 출력
print(*check_output, sep=" ")