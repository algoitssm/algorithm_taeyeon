import sys

sys.stdin = open("input.txt")

N, R = map(int, input().split())
tree = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b, d = map(int, input().split())
    tree[a].append([b, d])
    tree[b].append([a, d])
print(a, b, d, tree)

cnt = 0
for i in range(len(tree)):
    while len(tree[i]) > 2:
        cnt += tree[i][1]
print(cnt)
