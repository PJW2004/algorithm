B,N,M=map(int, input().split())
items = {}
for _ in range(N):
    item_name,item_price = input().split()
    items[item_name] = int(item_price)
pay = 0
for _ in range(M):
    pay += items[input()]
print("acceptable" if B >= pay else "unacceptable")