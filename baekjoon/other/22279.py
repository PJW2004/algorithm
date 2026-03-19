import sys
data = []
for _ in range(int(input())):
    life, year = map(float, sys.stdin.readline().split())
    data.append(life*year)
print(f"{sum(data):.3f}")