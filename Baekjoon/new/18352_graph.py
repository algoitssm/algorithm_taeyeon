import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(idx, cnt):
    que = deque()
    que.append((idx, cnt))
    while que:
        idx, cnt = que.popleft()
        if cnt == k:
            my_list.append(idx)
            return
        for t in tree[idx]:
            if not visited[t]:
                visited[t] = 1
                que.append((t, cnt+1))

n, m, k, x = list(map(int, sys.stdin.readline().split()))
node_list = [list(map(int, sys.stdin.readline().split())) for i in range(m)]
tree = [[] for _ in range(n+1)]
for node in node_list:
    tree[node[0]].append(node[1])
cnt = 0
my_list = []
visited = [0 for i in range(n+1)]
visited[x] = 1
bfs(x, 0)
my_list.sort()
print(my_list)
if not my_list:
    print(-1)
else:
    for my in my_list:
        print(my)