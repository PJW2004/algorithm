import sys
input_stdin = sys.stdin.readline
tree_count = int(input_stdin())
tree_list = list(map(int, input_stdin().split()))
tree_list_count = len(tree_list)
# 다익 스트라 알고리즘인가.
print(max([tree_lemon - (tree_list_count - tree_index) 
           for tree_index, tree_lemon in enumerate(tree_list)]))