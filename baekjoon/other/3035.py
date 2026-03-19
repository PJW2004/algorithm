import sys
stdin=sys.stdin.readline
R,_,ZR,ZC=map(int, stdin().split())
for text_string in ["".join(map(lambda s: s*ZC, stdin().strip())) for _ in range(R)]:
    [print(text_string) for _ in range(ZR)]