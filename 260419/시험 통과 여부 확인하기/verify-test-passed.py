n = input()
try:
    n = int(n)
except ValueError as e:
    raise ValueError(f"정수를 입력해주세요. 입력: {n}") from e

if not 0<=n<=100:
    raise ValueError(f"0~100 조건에 부합하지 않습니다. {n}") from None

pass_score = 80
if pass_score<=n:
    print("pass")
else:
    # 몇점이 더 있어야 통과되는지를 "x more score"라는 메시지로 출력
    more_score = pass_score-n
    print(f"{more_score} more score")