def dfs(num):
    global cnt
    if len(tree[num]) < 1: # 트리의 값이 0인 경우 값을 추가
        cnt += 1
        return
    for j in tree[num]:
        dfs(j)

# 데이터 입력받기 
N = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(N)]
delete = int(input())

for i in range(N):
    if nums[i] != -1 and i != delete: # 지울 노드가 아니고 root가 아닌경우만 추가, 지울 노드를 중간에 연결 끊기 위해서
        tree[nums[i]].append(i)
    elif nums[i] == -1: # -1 인 경우에 root로 지정
        root = i
# print(tree)  # [[1, 2], [], [3], [], [5, 6], [], [7, 8], [], []]
cnt = 0
if root == delete:
    cnt = 0
else:
    dfs(root)
print(cnt)


"""
import sys
sys.stdin = open("input.txt")


N = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(N)]
for idx, num in enumerate(nums):
    # print(idx, num)
    if num == -1:
        num = -2  # 마지막 인덱스로 추가 안되게 하기 위해서
    tree[idx].append(num)
    tree[num].append(idx)
# print(tree)
cnt = 0
for idx, num in enumerate(nums):
    if idx != 0 and len(tree[idx]) == 1:
        cnt += 1
# print(cnt)

delete = int(input())
node = [[] for _ in range(N)]
for idx, num in enumerate(nums[delete:N], start=delete):
    # print(idx, num)
    if num == -1:
        num = -2  # 마지막 인덱스로 추가 안되게 하기 위해서
    node[idx].append(num)
    node[num].append(idx)
# print(node)
counter = 0
for idx, num in enumerate(nums[delete:N], start=delete):
    if idx != 0 and len(node[idx]) == 1:
        counter += 1
# print(counter)
if cnt <= counter:
    print(cnt - counter + 1)
else:
    print(cnt - 1)
"""
