import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(start, length):
    que = deque()
    que.append((start, length))
    visited = [-1] * (N + 1) # 방문표현 노드가 1개일때 틀림, -1로 설정
    visited[start] = 0
    max_len = (0, 0)
    while que:
        start, length = que.popleft()
        for node, wei in tree[start]: # 루트에 인접한 아이들 체크
            if visited[node] == -1: # 방문 안한 경우 
                visited[node] = visited[start] + wei # 값 변경 + 가중치
                que.append((node, visited[node]))
            if visited[node] > max_len[1]:
                max_len = (node, visited[node])

    return max_length

N = int(input()) # 노드의 개수
tree = [[] for _ in range(N+1)] # 트리 연결 상태
for _ in range(N-1):
    root, child, weight = map(int, input().split())
    tree[root].append((child, weight))
    tree[child].append((root, weight))
# print(tree) # 트리
max_length = bfs(1, 0) # 가장 큰 가중치 찾기
# print(max_line) # 9
result = bfs(max_length[0], 0) # 거기서 다시 시작
print(result[1]) #처음에 visited = 1

# n이 1일때..?