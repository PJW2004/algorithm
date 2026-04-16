# 제한 조건
def read_input(str_number:str) -> int:
    int_number = int(str_number)
    if not 1<=int_number<=100:
        raise ValueError("제한 조건")
    return int_number

# 첫줄 공백을 사이에 두고
a,b=map(read_input, input().split())

print(b,a)