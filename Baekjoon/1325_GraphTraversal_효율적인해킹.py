from collections import deque


def bfs(col):
    que = deque()
    que.append(col)
    visited[col] = 1
    cnt = 0  # 해킹되는 수
    while que:
        hack = que.popleft()
        for i in range(N):
            if adj[col][i] == 1 and visited[col] == 0:
                visited[col] = 1
                que.append(i)
                cnt += 1
    return cnt


N, M = map(int, input().split())
adj = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(1, N):
    n1, n2 = map(int, input().split())
    adj[n2][n1] = 1

result = []
max_v = 0

visited = [0 for _ in range(N + 1)]
# print(adj)
for i in range(1, N + 1):
    hacker = bfs(i)
    if max_v == hacker:
        result.append(i)
    if max_v < hacker:
        max_v = hacker
        result = []
        result.append(i)
print(*result)
