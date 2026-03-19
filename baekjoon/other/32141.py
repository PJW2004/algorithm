n,h=map(int,input().split())
for index, demage in enumerate(list(map(int, input().split()))):
    h -= demage
    if h <= 0:
        print(index+1)
        break
if h > 0:
    print(-1)