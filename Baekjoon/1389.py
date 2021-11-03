import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(m)]
graph = [[0 for _ in range(n)] for _ in range(n)]
for friend in friends: # 행렬생성
    graph[friend[0] - 1][friend[1] - 1] = 1
    graph[friend[1] - 1][friend[0] - 1] = 1


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][k] and graph[k][j]:
                if graph[i][j] != 0: # 원래 연결지점이 0이 아닌경우
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
                else:
                    graph[i][j] = graph[i][k] + graph[k][j]
total = 50000

for i in range(len(graph)):
    if total > sum(graph[i]):
        total = sum(graph[i])
        result = i + 1
print(result) # 인덱스 맞추기 위해서
