from collections import deque
from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(arr):
    drow = [1, -1, 0, 0, 0, 0]
    dcol = [0, 0, 1, -1, 0, 0]
    dtop = [0, 0, 0, 0, 1, -1]
    day = 0 # 첫날
    while que:
        day += 1 # que 없을 때까지 day+1 같이 움직임
        for i in range(len(que)):
            top, col, row = que.popleft()
            for j in range(6):
                nrow = row + drow[j]
                ncol = col + dcol[j]
                ntop = top + dtop[j]
                if 0 <= ntop < H and 0 <= ncol < N and 0 <= nrow < M and arr[ntop][ncol][nrow] == 0:
                    arr[ntop][ncol][nrow] = 1 # 익은 토마토로 변경
                    que.append([ntop, ncol, nrow])

    for i in range(H): # 행 N
        for j in range(N): # 열 M
            for k in range(M):
                if arr[i][j][k] == 0: # 안 익은 토마토 있는 경우 -1
                    return -1
    return day - 1


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# print(arr[1][2][4])
que = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                que.append([i, j, k]) # 익지 않은 토마토 위치
# print(que)
print(bfs(arr))
