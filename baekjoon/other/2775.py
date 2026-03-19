# a 층의 b호에 살려면 자신의 아래(a-1) 층의 1호부터 b까지의 사람들의 수의 합만큼  사람들을 데려와 살아야 한다.
# k층에 n호에는 몇명이 살고 있는지 출력하라.
# 아파트에는 0층부터 있다.
# 각층은 1호부터 있고.
# 0층의 i호에는 i명이 산다. <- 이게 힌트인거 같은데.
test_case = int(input())
apart = [[0]*15 for _ in range(15)] # n <= 14
for i in range(15):
    apart[i][1] = 1 # i층 1호
    apart[0][i] = i # 0층 i호

for i in range(1, 15): # 1층 부터 14층
    for j in range(2, 15): # 2호 부터 14호
        apart[i][j] = apart[i][j - 1] + apart[i - 1][j]
for _ in range(test_case):
    k = int(input()) # 층
    n = int(input()) # 호
    # 다이나믹 프로그램을 DP 라 부르는 구나.
    print(apart[k][n])