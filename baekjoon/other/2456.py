import sys
input_stdin = sys.stdin.readline
candidates = {"1": [], "2": [], "3": []}
for _ in range(int(input_stdin())):
    # 회장이 유일하게 결정되는 경우에는 회장으로 결정된 후보의 번호와 최고 점수를 출력
    # 유일하게 결정할 수 없는 경우에는 0과 최고 점수를 출력
    a,b,c=map(int, input_stdin().split())
    candidates["1"].append(a)
    candidates["2"].append(b)
    candidates["3"].append(c)

def candidates_count_manager(candidates:dict, counter:int):
    _candidates = {"candidates":[], "max_count":0}
    for key, value in candidates.items():
        if sum(value) != max(candidates_array):
            continue
        if _candidates["max_count"] < value.count(counter):
            _candidates["candidates"] = [key]
            _candidates["max_count"] = value.count(counter)
        elif _candidates["max_count"] == value.count(counter):
            _candidates["candidates"].append(key)
    return _candidates

candidates_array = [sum(candidates["1"]), sum(candidates["2"]), sum(candidates["3"])]
if candidates_array.count(max(candidates_array)) == 1:
    print(f"{candidates_array.index(max(candidates_array))+1} {max(candidates_array)}")
else:
    # 단, 점수가 가장 큰 후보가 여러 명인 경우에는 3점을 더 많이 받은 후보를 회장으로 결정하고, 
    # 3점을 받은 횟수가 같은 경우에는 2점을 더 많이 받은 후보를 회장으로 결정한다. 
    # 그러나 3점과 2점을 받은 횟수가 모두 동일하면, 
    # 1점을 받은 횟수도 같을 수밖에 없어 회장을 결정하지 못하게 된다.
    candidates_three = candidates_count_manager(candidates, 3)
    candidates_two = candidates_count_manager(candidates, 2)

    if len(candidates_three["candidates"]) == 1:
        candidates_index = candidates_three["candidates"][0]
        print(f"{candidates_index} {max(candidates_array)}")
    elif len(candidates_two["candidates"]) == 1:
        candidates_index = candidates_two["candidates"][0]
        print(f"{candidates_index} {max(candidates_array)}")
    else:
        print(f"0 {max(candidates_array)}")