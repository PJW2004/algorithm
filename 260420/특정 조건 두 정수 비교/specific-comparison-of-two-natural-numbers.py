# 책으로 치면 1장 > 용어집 > 2장 순서로 제본 되었었음.
# 파이썬 관행은:
# 1. import
# 2. 함수/클래스 정의
# 3. main() 또는 if __name__ == "__main__" 임.
def bounded_token(token: str, left: int, right: int) -> int:
    try:
        value = int(token)
    # except ValueError as e:
        # 정수를 입력받아.
        # raise ValueError(f"정수를 입력해 주세요. 입력: {token!r}") from e
    except ValueError:
        # 개발자가 디버깅할 때는 좋지만, 최종 사용자에게는 같은 이야기를 영어와 한국어로 두번 듣는 셈.
        # 무엇이 잘못 됐나, 보단 사용자가 뭘 잘못 넣었나가 중요함.
        raise ValueError(f"정수를 입력해 주세요. 입력: {token!r}") from None
    if not left<=value<=right:
        # 제한조건
        # raise ValueError(f"제한조건({left}<=value<={right})에 부합하지 않습니다. 입력: {value}") from None
        # 여기서도 from None 은 무의미
        raise ValueError(f"제한조건({left}<=value<={right})에 부합하지 않습니다. 입력: {value}")
    return value

# 알고리즘 문제 풀이라서 문제 요구사항을 추적하려는 목적이라면 그 주석들 도크 스트링으로 모아둬라.
"""
입력: ~
출력: ~
"""

# 공백을 사이에 두고 주어짐
# tokens:list = input().split()
# 반만 말을 해줌.
# 타입힌트의 주요 독자는 IDE와 타입체커.
# 도구들이 이미 list[str] 을 추론함.
# 힌트는 함수 시그니처나 복잡한 자료구조처럼 추론이 어려운 곳에 아껴 쓰는 게 경제적.
tokens: list[str] = input().split()
if len(tokens) != 2:
    # 두개의
    # raise ValueError(f"공백을 사이로 2개만 입력하세요. 입력: {tokens}") from None
    # 숨길 예외 없음.
    # 에러는 안나고 __suppress_context__ = True 가 세팅되기만 함.
    raise ValueError(f"공백을 사이로 2개만 입력하세요. 입력: {tokens}")

# 리스트 컴프리헨션
# 제한 조건 1~100
# A,B = [bounded_token(token, 1, 100) for token in tokens]
# 이거 햇갈렸는데 할거면 그냥 소문자로 하라네.
a, b = [bounded_token(token, 1, 100) for token in tokens]

# 첫 번째 수가 더 작으면
# 두 개의 수가 같으면
# check_values = [A < B, A == B]

# # 맞으면 1 아니면 0
# check_output = map(int, check_values)

# # 결과값 두 개를 공백을 사이에 두고 출력
# print(*check_output, sep=" ")

# 출고완료, 배송 중 이라는 단계명만 적혀있고 내용물이 뭔지는 안적힌 상황.
# 게다가 한 줄씩만 쓰이고 버려지는 임시 변수라 수명도 짧음
print(int(a < b), int(a == b))