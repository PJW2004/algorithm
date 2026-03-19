import sys
# 입력은 20행으로 구성된다.
w_university = []
for _ in range(0,10):
    w_university.append(int(sys.stdin.readline()))
k_university = []
for _ in range(0,10):
    k_university.append(int(sys.stdin.readline()))
# 상위 3명의 점수 합산
print(f"{sum(sorted(w_university, reverse=True)[0:3])} {sum(sorted(k_university, reverse=True)[0:3])}")