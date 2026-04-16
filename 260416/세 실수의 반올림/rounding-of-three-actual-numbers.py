a:float = float(input())
b:float = float(input())
c:float = float(input())
if (not 0<=a)and(not 0<=b)and(not 0<=c):
    raise
if (not a<=1000)and(not b<=1000)and(not c<=1000):
    raise
a = round(a,3)
b = round(b,3)
c = round(c,3)
for output in [a,b,c]:
    print(f"{output:.3f}")