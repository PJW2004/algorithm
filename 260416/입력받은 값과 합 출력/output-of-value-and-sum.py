# 제한 조건 제한 조건
def bounded_int(text: str):
    try: # 예외 체이닝
        value = int(text)
    except ValueError as e:
        raise ValueError(f"정수로 변환할 수 없는 입력: {text!r}") from e
    if not 1<=value<=100:
        raise ValueError(f"1~100 범위를 벋어남: {value}")
    return value

# 첫번째 줄에 정수 공백 사이에
tokens = input().split()

# 리스트 컴프리헨션 이었나
values = [bounded_int(token) for token in tokens]
if 2 < len(values):
    raise ValueError(f"정수 공백 사이로 2개를 넘어섰습니다. 입력 개수: {len(values)}")

print(values[0], values[1], sum(values))