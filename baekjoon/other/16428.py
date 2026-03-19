# 어떤 정수 q와 r에 대해 A = qB + r 로 나타낼 수 있을때,
# q를 몫 r을 나머지라고 한다.
# r은 B 의 절대값 보단 작고 0보단 크다.
# A=2, B=1 
a,b=map(int, input().split())
# print(A//B)
# print(A%B)
# 목표는 유클리드 나눗셈.
# 파이썬은 내림 방식
c, d = divmod(a,b) # 몫과 나머지.
if a != 0 and d < 0:
    c, d = c+1, d-b
print(c)
print(d)