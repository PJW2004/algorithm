# n 의 크기는 1보다 크거나 같고.
# 1,000,000 보다 작거나 같다네.

# 그러면 맨 뒷자리 숫자부터 시작하는게 좋지 않을까.
# 해봤는데, 아래의 경우가 생김.
# -> 거짓 양성 : 실제로는 생성자가 아닌데 생성자라고 판단.
#               반례 : n=110
#               실제계산 : 109 + (1+0+9) = 119
# -> 거짓 음성 : 실제로는 생성자가 있는데도 놓침.
#               반례 : n = 119
#               실제계산 : 109 + (1+0+9) = 119
n = int(input())
out = 0
for number in range(0,n):
    # 0보다 크다.
    _sum = number
    for number_chunk in str(number):
        _sum += int(number_chunk)
    if n == _sum:
        out = number
        break
print(out)