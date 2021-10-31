import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split()) # 집하장 개수  # 간선 수
route_list = [list(map(int, input().split())) for _ in range(m)]
tree = [[[9999, 9999] for _ in range(n+1)] for _ in range(n+1)]
for route in route_list:
    tree[route[0]][route[1]] = [route[2], route[1]] #time, 도착 정점
    tree[route[1]][route[0]] = [route[2], route[0]]
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: # 같은 경우 계산 안할 예정이니
                tree[i][j] = [9999, '-']
            elif tree[i][j][0] > tree[i][k][0] + tree[k][j][0]:
                tree[i][j] = [tree[i][k][0] + tree[k][j][0], tree[i][k][1]]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(tree[i][j][1], end = ' ')
    print()