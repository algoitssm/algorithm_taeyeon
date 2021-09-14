import sys
sys.stdin = open('input2.txt')
from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    visited = [0] * (N + 1)
    while que:
        start = que.popleft()
        for node in tree[start]:
            if visited[node] == 0:
                visited[node] = visited[start] + 1
                que.append(node)

    for i in range(2, N+1):
        if len(tree[i]) != 1:
            visited[i] = 0
    return sum(visited)

N = int(input())
tree = [[] for _ in range(N+1)] # 트리 연결 상태
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
print(tree)
# print(bfs(1)) 홀짝.구분
if bfs(1) % 2 == 0:
    print('No')
else:
    print('Yes')

