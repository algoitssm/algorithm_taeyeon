from collections import deque


def bfs(row, col):
    time = 10001
    que = deque()
    que.append((row, col))
    while que:
        row, col = que.popleft()
        if maze[row][col] == 2:  # 그림 마주치는 경우
            time = visited[row][col] + (N - row - 1) + (M - col - 1)
        if row == N - 1 and col == M - 1:  # 최종 목적지 도착하는 경우
            if visited[row][col] < time:
                return visited[row][col]
        for i in range(4):  # 이외, 벽이 아닌 경우
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if (
                0 <= nrow < N
                and 0 <= ncol < M
                and visited[nrow][ncol] == 0
                and (maze[nrow][ncol] == 0 or maze[nrow][ncol] == 2)
            ):
                visited[nrow][ncol] = visited[row][col] + 1
                que.append((nrow, ncol))
    if time > T:
        return "Fail"
    return time


N, M, T = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

drow = [0, 0, -1, 1]
dcol = [1, -1, 0, 0]


print(bfs(0, 0))  # 0, 0 에서 시작
