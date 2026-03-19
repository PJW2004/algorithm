# 이항계수란 주어진 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 개수를 의미한다.
# nCk = n!/(n-k)!k!
def factorial(n:int):
    if n <= 1: # 0! 과 1! 고려.
        return 1
    return n * factorial(n-1)
n,k=map(int, input().split())
print(int(factorial(n)/(factorial(n-k)*factorial(k))))