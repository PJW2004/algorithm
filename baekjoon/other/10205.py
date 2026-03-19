k = int(input())
printing = []
for _ in range(k):
    hydra_head_cnt = int(input())

    # 단순히 머리를 자르는 것 'c'
    # 자르고 지혈하는 것  'b'
    for s in input():
        match s:
            case "c":
                hydra_head_cnt += 1
            case "b":
                hydra_head_cnt -= 1
    
    printing.append(hydra_head_cnt)

for idx, data in enumerate(printing):
    print(f"Data Set {idx+1}:\n{data}")
    if idx+1 != k:
        print("")