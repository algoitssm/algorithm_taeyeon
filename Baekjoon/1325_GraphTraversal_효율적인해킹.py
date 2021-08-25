import sys
from collections import deque


def bfs(row):
    visited = [0 for _ in range(N + 1)]
    cnt = 1
    que = deque()
    que.append(row)
    visited[row] = 1
    while que:
        com = que.popleft()
        for i in adj[com]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                que.append(i)
    # return sum(visited)
    return cnt


N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]

for _ in range(1, N):
    n1, n2 = map(int, sys.stdin.readline().split())
    adj[n2].append(n1)  # 오른쪽에 입력받은 컴퓨터 기준 [[], [3], [3], [4, 5], [], []]

result = [bfs(i) for i in range(N)]

for i in range(len(result)):
    if result[i] == max(result):
        print(i, end=" ")
