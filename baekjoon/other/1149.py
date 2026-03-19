count = int(input())

'''
3 (n 집의 개수)
      r  g  b
1번집 26 40 83
2번집 49 60 57
3번집 13 89 99

1번집은 r(26) 로 지정
1번집은 2번 집과 색이 같으면 안되므로 g(60) 와 b(57) 로 나뉨
N번 집의 색은 N-1번 집의 색과 같지 않아야 하므로 g(60)
3번 집의 색은 N-1번 (2번) 집의 색 g(60) 과 같지 않아야 하므로 r(13) 선택
그리고 그 비용의 최솟값을 구해야 한다.
'''
s = 0
back_rgb = ""
for _ in range(count):
    r, g, b = input().split(" ")
    rgb = [int(r),int(g),int(b)]

    if (min(rgb) == rgb[0]) and (back_rgb != "r"):
        s += rgb[0]
        back_rgb = "r"
    elif (min(rgb) == rgb[1]) and (back_rgb != "g"):
        s += rgb[1]
        back_rgb = "g"
    else:
        s += rgb[2]
        back_rgb = "b"
print(s)