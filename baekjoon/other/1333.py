album_count, song_time, call_time = map(int, input().split())
upper_call_time = album_count*(song_time + 5) - 5

real_time = 0
while True:
    # 앨범 다 끝남
    if real_time > upper_call_time:
        print(real_time)
        break
    # 곡 사이 5초 휴식
    if (real_time % (song_time + 5)) >= song_time:
        print(real_time)
        break
    real_time += call_time