import math

n = int(input().strip())

# k = ceil((sqrt(8n+1)-1)/2)
k = math.ceil((math.sqrt(8*n + 1) - 1) / 2)

# T_{k-1}
t_prev = (k - 1) * k // 2

# pos, a, b
pos = n - t_prev
b = pos
a = (k + 1) - pos

print(a, b)