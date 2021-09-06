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
