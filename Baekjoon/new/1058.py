import sys
sys.stdin = open("input.txt")

n = int(input())
friends = [list(map(str, input())) for _ in range(n)]
graph = [[0 for _ in range(n)] for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif friends[i][j] == 'Y':
                graph[i][j] = 1
            elif friends[i][k] == 'Y' and friends[k][j] == 'Y':
                graph[i][j] = 1
result = 0
# 가장 친구가 많은 행으로 선택
for gra in graph:
    if result < sum(gra):
        result = sum(gra)
print(result)