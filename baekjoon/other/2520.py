# 먼저 팬케이크 반죽 몇개 만들수 있는지를 구하자.
# 다음으로 각 토핑을 몇개의 반죽에 놓을 수 있는지를 고민하자.
# kneading_list = [16/8,16/8,16/4,16/1,16/9]
# ?????? 1.7 과 1.77777777777 차이가 뭐임?
# kneading_list = [2,2,4,16,1.77]
import sys

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(tokens)
    try:
        t = next(it)  # 테스트 케이스 수
    except StopIteration:
        return

    out = []
    for _ in range(t):
        # 재료(우유, 노른자, 설탕, 소금, 밀가루)
        milk = next(it); yolk = next(it); sugar = next(it); salt = next(it); flour = next(it)
        # 토핑(바나나, 잼, 초코, 호두)
        banana = next(it); jam = next(it); choco = next(it); walnut = next(it)

        # 반죽 1장당 필요량: 우유 0.5, 노른자 0.5, 설탕 0.25, 소금 1/16, 밀가루 9/16
        # → 정수 연산으로 변환
        c  = milk * 2           # floor(milk / 0.5)
        y  = yolk * 2           # floor(yolk / 0.5)
        su = sugar * 4          # floor(sugar / 0.25)
        sa = salt * 16          # floor(salt / (1/16))
        f  = (flour * 16) // 9  # floor(flour / (9/16))

        cake = min(c, y, su, sa, f)

        # 토핑 개수 합
        topping = (banana // 1) + (jam // 30) + (choco // 25) + (walnut // 10)

        out.append(str(min(cake, topping)))

    print("\n".join(out))

if __name__ == "__main__":
    main()
