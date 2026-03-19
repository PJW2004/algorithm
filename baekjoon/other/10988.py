# 앞뒤가 똑 같은 팰린드롬
data = input()
if data == data[::-1]:
    print(1)
else:
    print(0)