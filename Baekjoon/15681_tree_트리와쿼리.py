import sys 

sys.setrecursionlimit(10000000)
sys.stdin = open("input.txt")


def solve(currentnode):
    visited[currentnode] = 1  # 방문 표현
    for node in tree[currentnode]:
        if visited[node] == 0:  # 루트가 아닌 경우 와 방문하지 않은 경우
            solve(node)
            visited[currentnode] += visited[node]


N, R, Q = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    tree[U].append(V)
    tree[V].append(U)
# print(tree)
solve(R)  # 루트 노드를 기준으로 방문 값 표현
for i in range(Q):
    U = int(input())
    # print(visited)
    print(visited[U])
