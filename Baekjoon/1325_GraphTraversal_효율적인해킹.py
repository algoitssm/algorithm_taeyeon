import sys
from collections import deque


def dfs(start):  # 시간초과 => 통과!!
    visited = [0 for _ in range(N + 1)]
    stack = [start]
    visited[start] = 1
    total = 0

    while stack:
        num = stack.pop()
        total += 1
        for i in adj[num]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
    return total


N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    adj[n2].append(n1)  # 오른쪽에 입력받은 컴퓨터 기준 [[], [3], [3], [4, 5], [], []]

max_v = 0
visited = [0 for _ in range(N + 1)]
result = []

# 여서부터는 성렬님 코드 참고

for i in range(1, N + 1):
    if visited[i]:
        continue
    total = dfs(i)
    if max_v < total:
        result = [i]
        max_v = total
    elif max_v == total:
        result.append(i)

print(*result)
