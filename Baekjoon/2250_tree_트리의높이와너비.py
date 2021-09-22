import sys

sys.stdin = open("input.txt")


def solve(root_node, level):
    global cnt
    if tree[root_node][0] != -1:
        solve(tree[root_node][0], level + 1)
    tree_idx_level[root_node][0] = cnt
    cnt += 1
    tree_idx_level[root_node][1] = level
    if tree[root_node][1] != -1:
        solve(tree[root_node][1], level + 1)


n = int(input())
tree_idx_level = [[0] * 2 for i in range(n + 1)]

tree = [[] for i in range(n + 1)]
root_list = [0 for i in range(n + 1)]
for i in range(n):
    node, left, right = list(map(int, input().split()))
    tree[node].append(left)
    tree[node].append(right)
    if left != -1:
        root_list[left] += 1
    if right != -1:
        root_list[right] += 1
root = 0
cnt = 1
# print(tree)
# print(root_list)
for i in range(1, n + 1):
    if root_list[i] == 0:
        root = i
solve(root, 1)  # 루트와 level
# print(tree_idx_level) # [[0, 0], [4, 1], [2, 2], [5, 2], [3, 3], [1, 3], [6, 3]]


max_level = []
for i in range(1, len(tree_idx_level)):
    max_level.append(tree_idx_level[i][1])
max_level_idx = max(max_level)  # level의 최대값
# print(max_level_idx)
result = [[] for i in range(max_level_idx + 1)]
for i in range(len(tree_idx_level)):
    for j in range(2, max_level_idx + 1):
        if tree_idx_level[i][1] == j:
            result[j].append(tree_idx_level[i][0])
print(result)  # 각level별로 가능한 idx 담은 리스트
final_result = [1, 1]
for i in range(len(result)):
    if len(result[i]) > 1:
        if final_result[1] < max(result[i]) - min(result[i]) + 1:
            final_result[1] = max(result[i]) - min(result[i]) + 1
            final_result[0] = i

print(*final_result)
