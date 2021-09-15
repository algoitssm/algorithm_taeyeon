import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(node):
    que = deque()
    que.append(node)
    cnt = 0
    while que:
        node = que.popleft()
        for i in tree[node]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1 # 이동한 국가의 수 count
                que.append(i)
    return cnt - 1 # 국가의 수가 아닌 탄 비행기의 수

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N + 1)] # 국가의 개수 기준으로!!!!!!!!!!
    visited = [0 for _ in range(N + 1)] # 국가의 개수 기준으로!!!!!!!!!!
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    # [-1, 2, -1]
    # [-1, 4, -1, -1, -1]
    print(bfs(1))