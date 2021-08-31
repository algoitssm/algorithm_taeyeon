from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(arr):
    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]
    day = 0 # 첫날
    while que:
        day += 1 # que 없을 때까지 day+1 같이 움직임
        for i in range(len(que)):
            row, col = que.popleft()
            for j in range(4):
                nrow = row + drow[j]
                ncol = col + dcol[j]
                if 0 <= nrow < N and 0 <= ncol < M and arr[nrow][ncol] == 0:
                    arr[nrow][ncol] = 1 # 익은 토마토로 변경
                    que.append([nrow, ncol])

    for i in range(N): # 행 N
        for j in range(M): # 열 M
            if arr[i][j] == 0: # 안 익은 토마토 있는 경우 -1
                return -1
    return day - 1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
que = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que.append([i, j]) # 익지 않은 토마토 위치
# print(que)
print(bfs(arr))