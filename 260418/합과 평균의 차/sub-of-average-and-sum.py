tokens = input().split()
if len(tokens) != 3:
    raise ValueError(f"공백을 기준으로 3개의 입력이 아닙니다. 입력: {len(tokens)}")
values = list(map(int, tokens))
if sum(values) % 3 != 0:
    raise ValueError("세 수의 합이 3의 배수가 아닙니다.")
if not all([1<=value<=100 for value in values]):
    raise ValueError("1-100 제한에 맞춰지지 않았습니다.")
print(sum(values))
print(sum(values)//3)
print(sum(values)-(sum(values)//3))