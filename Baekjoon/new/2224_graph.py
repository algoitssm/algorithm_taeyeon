import sys
from collections import deque
sys.stdin = open('input.txt')

def dfs(idx):
    que = deque()
    que.append(idx)
    while que:
        idx = que.popleft()
        if the[0] != idx:
            result.append((the[0], idx))
        for i in tree[idx]:
            if not visited[i]:
                dfs(i)

n = int(sys.stdin.readline())
thesis = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
tree = [[] for _ in range(70)]
for the in thesis:
    the[0] = ord(the[0]) - 65
    the[2] = ord(the[2]) - 65
    tree[the[0]].append(the[2])
result = []
for the in thesis:
    visited = [0 for _ in range(70)]
    dfs(the[0])
result = sorted(result, key=lambda x : (x[0], x[1]))
for i in range(len(result)):
    print(chr(result[i][0]+65)+' => '+chr(result[i][1]+65))