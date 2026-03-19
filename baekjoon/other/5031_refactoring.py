e,f,c = map(int,input().split())
e+=f
ans=0
while e >= c:
    e-=c
    e+=1
    ans+=1
print(ans)