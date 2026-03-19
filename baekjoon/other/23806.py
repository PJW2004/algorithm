# 가로 세로 * n 으로 하면 되겠다.
n = int(input())
# ============================
# n=3
# [0:14] * 3
# [0:2][3:11][12:14] * 9
# [0:14] * 3

# n=2
# [0:9] * 2
# [0:1][2:7][8:9] * 6
# [0:9] * 2

# n=1
# [0:4] * 1
# [0:0][1:3][4:4]* 3
# [0:4] * 1
# ============================
# [0:(5*n)-1] * n
# [0:n-1][n:(5*n)-n][(5*n)-(n-1):(5*n)-1] * (3*n)
# [0:(5*n)-1] * n
# ============================
for _ in range(n):
    text = ""
    for _ in range(0,5*n):
        text += "@"
    print(text)
for _ in range(3*n):
    text = ""
    for _ in range(0,n):
        text += "@"
    for _ in range(n,(5*n)-n):
        text += " "
    for _ in range((5*n)-n,5*n):
        text += "@"
    print(text)
for _ in range(n):
    text = ""
    for _ in range(0,5*n):
        text += "@"
    print(text)