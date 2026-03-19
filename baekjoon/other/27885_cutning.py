# 1. 문제에서 주어지는 모든 시각은 05시 00분 00초 이후이고, 23시 59분 01초 이전
# 2. 하루 동안 상행 열차와 하행 열차가 산성대로 건널목에 접근하는 시각이 주어졌을 때
from sys import stdin
input = stdin.readline
DAY = 86400

c, h = map(int, input().split())
timeline = []
for _i in range(c + h):
    h, m, s = map(int, input().split(':'))
    timeline.append(h * 60 * 60 + m * 60 + s)
timeline.sort()

prev = -40
total_passing = 0
"""
반례)
4 1
07:30:00
07:30:00
07:30:00
07:30:00
07:30:39
"""
for time in timeline:
    breakpoint()
    if time - prev >= 40:
        passing = 40
    else:
        passing = time - prev

    total_passing += passing
    prev = time

print(DAY - total_passing)