n,k=map(int, input().split())
measure=[]
for number in range(1, n+1):
    if n % number == 0:
        measure.append(number)
if len(measure) < k:
    print(0)
else:
    print(measure[k-1])