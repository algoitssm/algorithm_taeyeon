import sys

sys.stdin = open("input.txt")


def dfs(giga_node, giga_length):
    for node in tree[giga_node]:
        if visited[node[0]][0] == 0:  # 방문하지 않은경우
            visited[node[0]][0] = 1  # 방문 표현
            dfs(node[0], giga_length + node[1])
            visited[node[0]][1] = giga_length + node[1]


N, R = map(int, input().split())
tree = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))

giga_f = []
for i in range(len(tree)):
    if len(tree[i]) > 2:
        giga_f.append(i)
if len(giga_f) < 1:
    giga_node = N
else:
    giga_node = giga_f[0]

length = 0  # 기가로드를 통해 기가로드까지의 기둥 길이 구함
visited = [[0] * 2 for i in range(N + 1)]
for i in range(R, giga_node):
    for j in tree[i]:
        if visited[j[0]][0] == 0 and j[0] != R:
            length += j[1]
            visited[j[0]][0] = 1
visited[giga_node][0] = 1

dfs(giga_node, 0)

print(length, max(visited)[1])
