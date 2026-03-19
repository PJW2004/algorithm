import sys
request = list(map(int, sys.stdin.readline().split()))
if request == sorted(request):
    print("ascending")
elif request == sorted(request, reverse=True):
    print("descending")
else:
    print("mixed ")