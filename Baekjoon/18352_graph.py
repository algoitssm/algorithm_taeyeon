import sys
from collections import deque
sys.stdin = open('input.txt')

def solve(idx, cnt):
    que = deque()
    que.append((idx, cnt))
    while que:
        idx, cnt = que.popleft()
        if cnt == k:
            if idx == x: # 출발지점과 도착지점이 같은 경우 단방향의 경우 예외 케이스 처리
                continue
            result.append(idx)
        elif cnt < k:
            for i in tree[idx]:
                if not visited[i]:
                    visited[i] = 1
                    que.append((i, cnt+1))

n, m, k, x = list(map(int, sys.stdin.readline().split()))
node_list = [list(map(int, sys.stdin.readline().split())) for i in range(m)]
tree = [[] for _ in range(n+1)]
for node in node_list:
    tree[node[0]].append(node[1]) # 왼쪽을 기준으로 단방향 인접 리스트 생성
visited = [0 for _ in range(n+1)]
result = []
solve(x, 0)
result.sort() # 오름차순으로 출력한다
if not result:
    print(-1)
else:
    print(*result, sep='\n')