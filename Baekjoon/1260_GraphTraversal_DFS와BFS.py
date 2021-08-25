# 출력.........;;;;;;;;;;;;;;;;;;;

from collections import deque
from sys import stdin


def bfs(S):
    que = deque()
    que.append(S)
    visited_bfs[S] = 1  # 방문 표현
    while que:
        status = que.popleft()
        print(status, end=" ")  # 현재 위치한 노드 출력
        for i in range(V + 1):
            if adj[status][i] == 1 and visited_bfs[i] == 0:  # 노드 값 1이고 방문 안한경우
                visited_bfs[i] = 1  # 현재 노드 방문 표현
                que.append(i)


def dfs(S):
    visited_dfs[S] = 1
    print(S, end=" ")
    for i in range(V + 1):
        if adj[S][i] == 1 and visited_dfs[i] == 0:
            dfs(i)


V, E, S = map(int, input().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    n1, n2 = list(map(int, input().split()))
    adj[n1][n2] = 1
    adj[n2][n1] = 1
# print(adj)
visited_dfs = [0] * (V + 1)
visited_bfs = [0] * (V + 1)


dfs(S)
print()  # None안나오도록...?

bfs(S)
