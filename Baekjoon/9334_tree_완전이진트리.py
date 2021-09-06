from collections import deque
import sys

sys.stdin = open("input.txt")


N = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(N)]


def find(idx, nums):

    if len(nums) != 1:
        root = len(nums) // 2
        tree[idx].append(nums[root])  # 루트값 발견해주기

        find(idx + 1, nums[:root])  # 왼쪽
        find(
            idx + 1, nums[root + 1 :]
        )  # 오른쪽 # N지정하면 index오류발생.....................................
    else:
        tree[idx].append(nums[0])  # 루트값 발견해주기


find(0, nums)
for i in range(N):
    for j in tree[i]:
        print(j, end=" ")
    print()
