"""
4*4 큐브
1,2 -> 2,4 / 3,1 / 3,3
2,2 -> 4,1 / 4,3 / 3,4 / 1,4
3,2 -> 1,1 / 1,3 (행 기준에서 3(열) 은 -2 하고 행 +- 1 진행.) 
                 (행 기준에서 3(열) +2 는 없는 값이므로 진행 X.)
    / 2,4 / 4,4  (열 기준에서 2(행) 은 +2 하고 열 +- 1 진행.)
                 (열 기준에서 2(행) -2 는 없는 값이므로 진행 X.)
"""
for index in range(int(input())):
    # r : 열
    # c : 행
    n,r1,c1,r2,c2=map(int,input().split())
    batch_list=[]
    if r1 - 2 > 0:
        if c1+1 <= n:
            batch_list.append((r1-2,c1+1))
        if c1-1 > 0:
            batch_list.append((r1-2,c1-1))
    if r1 + 2 <= n:
        if c1+1 <= n:
            batch_list.append((r1+2,c1+1))
        if c1-1 > 0:
            batch_list.append((r1+2,c1-1))
    if c1 - 2 > 0:
        if r1+1 <= n:
            batch_list.append((r1+1,c1-2))
        if r1-1 > 0:
            batch_list.append((r1-1,c1-2))
    if c1 + 2 <= n:
        if r1+1 <= n:
            batch_list.append((r1+1,c1+2))
        if r1-1 > 0:
            batch_list.append((r1-1,c1+2))
    if (r2,c2) in batch_list:
        print(f"Case {index+1}: YES")
    else:
        print(f"Case {index+1}: NO")