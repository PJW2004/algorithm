# 부르트포스 알고리즘은 모든 경우를 계산 함.
# 각 가중치는 1,3,1,3 순으로 부여됨.
# 훼손된 숫자는 '*' 로 표기됨.
# -> 무작위 한자리.
# 전체를 더한 값의 10으로 나눈 나머지가 0이 되도록 해야함.
# 무작위 한자리가 비어 있으므로 경우의 수는 고작 9.
isbn=input()
m=0
m_index=0
for index, check in enumerate(isbn):
    if check == '*':
        m_index=index
        continue
    if index % 2 == 0:
        m += int(check)
    else:
        m += int(check)*3
if m_index%2 == 0:
    print(10-(m%10))
else:
    for number in range(0,10):
        if (m+number*3) % 10 == 0:
            print(number)
            break