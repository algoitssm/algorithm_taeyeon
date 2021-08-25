import sys

sys.setrecursionlimit(100000)


def dfs(col):
    for i in adj[col]:
        if parent[i] == 0:
            parent[i] = col
            dfs(i)


N = int(sys.stdin.readline())
adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

parent = [0 for _ in range(N + 1)]

dfs(1)

for i in range(2, N + 1):
    print(parent[i])

"""
import sys

sys.setrecursionlimit(100000)
from collections import deque


def bfs(col):
    que = deque()
    que.append(col)
    while que:
        par = que.popleft()
        for i in adj[par]:
            if visited[i] == 0:
                visited[i] == 1
                parent[i] == par
                que.append(i)
    return parent


N = int(input())
adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

parent = [0 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
bfs(1)
print()
for i in range(2, N + 1):
    print(parent[i])
"""
