"""
정수 n이 주어짐.
시험 등급:
    90점 이상 > A
    80점 이상 > B
    70점 이상 > C
    60점 이상 > D
    60점 미만 > F

제한 조건: 0<=n<=100
"""
token = input()
try:
    n = int(token)
except ValueError:
    raise ValueError(f"정수를 입력해주세요. 입력: {n!r}") from None

if n>=90:
    print("A")
elif n>=80:
    print("B")
elif n>=70:
    print("C")
elif n>=60:
    print("D")
else:
    print("F")