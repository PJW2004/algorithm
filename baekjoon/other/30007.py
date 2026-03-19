# 라면 공식
for _ in range(int(input())):
    a,b,x = map(int, input().split())
    w = a * (x-1) + b
    print(w)