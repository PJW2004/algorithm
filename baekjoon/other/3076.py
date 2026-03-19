r,c = map(int,input().split())
a,b = map(int,input().split())
# a*b 박스를 X 와 . 으로 만들어 두고.
# r열 c행으로 출력하면 되겠다.
box = []
for r_index in range(r):
    for _ in range(a): # r * a
        row = ""
        for c_index in range(c):
            if r_index % 2 == 0:
                if c_index % 2 == 0:
                    for _ in range(b): # c * b
                        row += "X"
                else:
                    for _ in range(b): # c * b
                        row += "."
            else:
                if c_index % 2 == 0:
                    for _ in range(b): # c * b
                        row += "."
                else:
                    for _ in range(b): # c * b
                        row += "X"
        box.append(row)
print("\n".join(box))