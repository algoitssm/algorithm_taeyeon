import sys

sys.stdin = open("input.txt")
from collections import deque


def solve(node1, node2):
    que = deque()
    que.append(node1)
    que.append(node2)
    visited[node1] = 1
    visited[node2] = 1
    while que:
        nodes = que.popleft()
        for node in tree[nodes]:
            if visited[node] == 1:  # 가장 먼저 두 node 모두 방문 한 경우 출력
                return node
            visited[node] = 1
            que.append(node)


T = int(input())
for tc in range(T):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[b].append(a)
    node1, node2 = map(int, input().split())  # 두 노드의 가장 가까운 노드 찾기

    print(solve(node1, node2))
