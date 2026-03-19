import sys
pixels_per_inch_list = []
for index in range(0,int(sys.stdin.readline())):
    monitor_weight_pixels, monitor_hight_pixels = map(int, sys.stdin.readline().split())
    # 모든 모니터의 크기는 77인치로 동일하다.
    pixels_per_inch = ((monitor_weight_pixels**2 + monitor_hight_pixels**2)**0.5) / 77
    # N개의 줄에 걸쳐 모니터의 번호를 PPI가 높은 순으로 한 줄에 하나씩 출력한다.
    pixels_per_inch_list.append((pixels_per_inch, index+1))
# PPI가 동일한 경우 번호가 더 작은 모니터를 먼저 출력한다.
pixels_per_inch_list.sort(key=lambda x: (-x[0], x[1]))
for pixels_per_inch in pixels_per_inch_list:
    print(pixels_per_inch[1])