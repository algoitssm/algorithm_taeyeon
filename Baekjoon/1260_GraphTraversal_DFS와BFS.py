from collections import deque
from sys import stdin


def bfs(S):
    que = deque()
    que = [S]  # que에 초기값 저장
    visited_dfs[S] = 1  # 초기 S
    n = 0
    while que:
        status = que.pop(0)
        print(status, end=" ")
        for i in range(V + 1):
            if adj[status][i] == 1 and visited_dfs[i] == 0:  # network연결되어 있으면서 방문 안한 경우
                visited_dfs[i] = 1  # 방문으로 체크
                que.append(i)


def dfs(S):
    visited_dfs[S] = 1
    print(S, end=" ")
    for i in range(1, V + 1):
        if adj[S][i] == 1 and visited_dfs[i] == 0:
            dfs(i)


V, E, S = map(int, input().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    n1, n2 = list(map(int, input().split()))
    adj[n1][n2] = 1
    adj[n2][n1] = 1

visited_dfs = [0] * (V + 1)
visited_bfs = [0] * (V + 1)

# bfs(S)
# dfs(S)
