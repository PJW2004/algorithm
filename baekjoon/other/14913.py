# 등차수열
# a_n = a + (n-1)d
# a > 첫째 항
# n > 항 수
# d > 공차
# ❌ 틀림
# a,d,k=map(int, input().split())
# if d < 0:
#     if k > a:
#         # 반례 : 10(a) -2(d) 6(k) > 3
#         print("X")
#     else:
#         print(k//abs(d))
# else:
#     if (k-d)%a == 0:
#         # 반례 : 3 2 11 > 5
#         print((k-a)//d+1)
#     else:
#         print("X")

# 처음 풀이
a, d, k = map(int, input().split())

# d == 0인 경우는 항이 모두 동일하므로 별도로 처리
# ✅ 정답
if d == 0:
    if k == a:
        print(1)
    else:
        print("X")
else:
    n_minus_1, r = divmod(k - a, d)
    if r == 0 and n_minus_1 >= 0:
        print(n_minus_1 + 1)
    else:
        print("X")
