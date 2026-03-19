# 다른 사람 코드다, 니 코드 아니다.
a,o,b=input().split()
print('true'if (o=='AND'and a==b=='true')or(o=='OR'and not a==b=='false')else'false')