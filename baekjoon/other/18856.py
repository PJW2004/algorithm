import sys
input_stdin = sys.stdin.readline
a_size = int(input_stdin())
print(a_size)
print(' '.join(map(str, [1,2] + list(range(3,a_size)) + [997])))