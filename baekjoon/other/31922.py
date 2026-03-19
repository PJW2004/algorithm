import sys
division_1,division_2,shake=map(int,sys.stdin.readline().split())
print(max([division_1+shake,division_2]))