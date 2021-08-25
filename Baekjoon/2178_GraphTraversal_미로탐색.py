# dfs...cnt 1의 모든 수 sum ...........
from collections import deque

# 최단거리는 bfs!~!~!~!~!
def maze_visit(row, col):
    que = deque()
    que.append((row, col))

    while len(que) > 0:
        row, col = que.popleft()
        for i in range(4):  # 방향 설정
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < N and 0 <= ncol < M and maze[nrow][ncol] == 1:  # 범위 안에 존재하고 maze값이 1인 경우
                maze[nrow][ncol] = maze[row][col] + 1  # 이전의 값에 추가로 + 1
                que.append((nrow, ncol))  # 가능한 경로 추가
    return maze[N - 1][M - 1]  # 마지막 N,M에 도착하면 그 값 출력


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
dcol = [-1, 0, 0, 1]
drow = [0, 1, -1, 0]
# cnt = 0
# visited = [[0] * M for _ in range(N)]

print(maze_visit(0, 0))
