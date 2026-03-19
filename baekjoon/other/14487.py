# 마을의 수
n = int(input())
# 이런 효도쟁이!
villages = list(map(int, input().split()))
if len(villages) != n:
    raise ValueError()
print(sum(villages)-max(villages))