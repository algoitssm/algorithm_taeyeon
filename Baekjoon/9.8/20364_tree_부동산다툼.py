import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(que):
    global possible
    while que:
        node = que.popleft()
        if occupy[node] == 1 or occupy[node // 2] == 1: # 첫번째 값을 찾아야함...!!!!!
            possible = node // 2
        else:
            occupy[node] = 1
            possible = 0
        print(possible)

N, Q = map(int, input().split())
occupy = [[0] for _ in range(N + 1)]
que = deque()
for i in range(Q):
    que.append(int(input()))
bfs(que)