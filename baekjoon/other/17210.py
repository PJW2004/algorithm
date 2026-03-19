# 연속된 두 문은 같은 방식으로 열 수 없다.
# 2의 배수 번호인 문들은 서로 같은 방식으로 열어야 한다.
# 3의 배수 번호인 문들은 서로 같은 방식으로 열어야 한다.
# 이렇게 되면 N >= 6이면 규칙을 만족하는 방법이 존재하지 않으니,
# "Love is open door" 출력
n = int(input())
door = int(input())
if n >= 6:
    print('Love is open door')
else:
    for _ in range(n-1):
        if door:
            door -= 1
        else:
            door += 1
        print(door)