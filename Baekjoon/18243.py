import sys
from collections import deque
sys.stdin = open("input.txt")

def bfs(start):
    que = deque([start])
    while que:
        start = que.popleft()
        for i in graph[start]:
            if not visited[i]:
                visited[i] = visited[start] + 1
                que.append(i)

n, k = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(k)]
graph = [[] for _ in range(n)]
for friend in friends:
    graph[friend[0] - 1].append(friend[1] - 1)
    graph[friend[1] - 1].append(friend[0] - 1)
#print(graph)
result = 'Small World!'
for i in range(n):
    visited = [0 for _ in range(n)]
    bfs(i)
    # 0 으로방문을 안하는 경우이거나 거리가 6보다 큰경우 판단
    # print(visited)
    if max(visited) > 6 or (0 in visited):
        result = 'Big World!'
        break
print(result)