import sys

for _ in range(int(input())):
    # 층 수, 각 층의 방 수, 몇 번째 손님
    H, W, N = map(int, sys.stdin.readline().split())
    if N % H == 0:
        floor = H
        room_number = "{0:02d}".format(N // H)
    else:
        floor = N % H
        room_number = "{0:02d}".format(N // H + 1)
    print(f"{floor}{room_number}")