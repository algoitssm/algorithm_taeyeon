from collections import deque


def bfs():

    while que:
        row, col = que.popleft()

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < N and 0 <= ncol < M and tomato[nrow][ncol] == 0:
                tomato[nrow][ncol] = tomato[row][col] + 1
                que.append((nrow, col))


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for i in range(N)]
# print(tomato)
drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]
que = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            que.append((i, j))
bfs()
result = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)
