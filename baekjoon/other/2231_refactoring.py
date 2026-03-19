def digit_sum(x:int) -> int:
    return sum(int(ch) for ch in str(x))

n = int(input())

start = max(0, n-9*len(str(n)))
# -> 이전에는 최악에선 거의 백만번 검사.
#    어떤 수 "x" 의 분해합은 "x + 각 자리수 합" 이고, 
#    자리수 합의 최댓값은 "9 * 자릿수(d)"
#    예 : n = 1,000,000 이면 자릿수 "d=7", 최대 가산분은 "9*7=63"
#         즉, 생성자가 있더라도 "n - 9*d" 아래에는 존재할 수 없음.
# -> 9가 있는 이유는 10진수의 최댓값이 9이기 때문.
#    자릿수가 3개 라는 것은 9 + 9 + 9 로 계산 된다는 것.
answer = 0
for x in range(start,n):
    # O(O(n))
    if x + digit_sum(x) == n:
        answer = x
        break
print(answer)