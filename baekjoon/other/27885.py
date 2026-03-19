# 1. 문제에서 주어지는 모든 시각은 05시 00분 00초 이후이고, 23시 59분 01초 이전
# 2. 하루 동안 상행 열차와 하행 열차가 산성대로 건널목에 접근하는 시각이 주어졌을 때
crossing_gate_initialize=24*3600

upstream_train_count,down_train_count=map(int, input().split())
# 상행 열차 수
train_second_list=[]
second_list=[]
for _ in range(upstream_train_count+down_train_count):
    hour,miniute,second=map(int,input().split(":"))
    train_second=hour*3600+miniute*60+second
    if train_second_list:
        if train_second_list[-1] + 40 + 60 > train_second + 40:
            train_second_list.append(train_second)
        else:
            if len(train_second_list) == 1:
                second_list.append(40*2)
            else:
                # 곂치는 부분 구하기.
                second_list.append((train_second_list[-1]+40)-train_second_list[0])
            train_second_list=[]
    else:
        train_second_list.append(train_second)
if train_second_list:
    second_list.append((train_second_list[-1]+40)-train_second_list[0])

# 하루 동안 상행 열차와 하행 열차가 산성대로 건널목에 접근하는 시각이 주어졌을 때, 
# 몇 초 동안 산성대로 건널목의 차단기가 올라가는지 구해주세요.

# e.g)
# 열차가 산성대로 건널목에 접근하면, 40초 후에 완전히 빠져나갑니다. 
# 예를 들어, 열차가 11시 10분 15초에 산성대로 건널목에 접근한 경우
# 11시 10분 15초부터 11시 10분 55초가 될 때까지 열차는 산성대로 건널목을 통과하게 됩니다.
# 11시 10분 55초가 되었을 때, 완전히 빠져나갑니다.
print(crossing_gate_initialize-sum(second_list))