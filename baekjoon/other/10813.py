# 바구니 N개
# 바꾸려는 횟수 M번
n,m=map(int, input().split())
# 1번 부터 N번까지의 번호
default_basket = list(range(1, n+1))
for _ in range(m):
    i,j=map(int, input().split())
    # [1,2,3,4,5]
    # 1, 2
    # [2,1,3,4,5]
    # 3,4
    # [2,1,4,3,5]
    # 1,4
    # [3,1,4,2,5]
    memory = default_basket[i-1]
    default_basket[i-1] = default_basket[j-1]
    default_basket[j-1] = memory
print(" ".join(map(str, default_basket)))