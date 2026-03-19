# [빨, 파, 노]
# [1,2,3]

# 4
# [1,1,1,1][1,2,2,1][1,2,2,1][1,1,1,1]

_ = input()
for _ in range(int(input())):
    out = int(input().split()[0])%3
    if out:
        print(out)
    else:
        print(3)