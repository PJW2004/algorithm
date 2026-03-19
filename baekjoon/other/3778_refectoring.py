import sys
input_stdin = sys.stdin.readline
w
# 어떻게 하면 4736ms 나오냐.
# 예제 입력 공백 순간 뭔가했네.
output_list = []
for index in range(1, int(input_stdin())+1):
    # 애너그램 거리가 다익스트라로 모든 단어를 비교해야 할것 같지만
    # 빈도수로 계산하면 되는구나.
    alphabet_a = input_stdin()
    alphabet_b = input_stdin()
    # print(f'Case #{index}: {sum([abs(alphabet_a.count(alphabet) - alphabet_b.count(alphabet)) for alphabet in set(alphabet_a + alphabet_b)])}')
    output_list.append(f'Case #{index}: {sum([abs(alphabet_a.count(alphabet) - alphabet_b.count(alphabet)) for alphabet in set(alphabet_a + alphabet_b)])}')
output_stdout('\n'.join(output_list))