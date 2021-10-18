import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(idx):
    que = deque()
    que.append(idx)
    while que:
        idx = que.popleft()
        for i in tree[idx]:
            if not visited[i]:
                visited[i] = 1
                que.append(i)
    print(*visited)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
tree = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            tree[i].append(j) # 단방향 인접리스트 생성
for i in range(n): # 행을 기준으로 돌아본다
    visited = [0 for _ in range(n)]
    bfs(i)