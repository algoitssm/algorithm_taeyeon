from collections import deque
import sys
sys.stdin = open('input.txt')

def time(time):
    if time % 2 == 0: # 짝수번째 시간에는 0초로 폭발한 폭탄을 다시 3으로 채워준다.
        for a in range(R):
            for b in range(C):
                if arr[a][b] == 0:
                    arr[a][b] = 3
                else:
                    arr[a][b] -= 1
    elif time % 2 == 1:
        for x in range(R):
            for y in range(C):
                if arr[x][y] == 1:
                    bfs(x, y)
                else:
                    arr[x][y] -= 1
                    if arr[x][y] <= 0: # 음수 무조건 0으로 출력
                        arr[x][y] = 0
    return arr

def bfs(row, col): # 방향에 조절 1인경우에만 전부 4방향 전부 1로 변경
    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]
    que = deque()
    que.append((row, col))
    arr[row][col] = 0
    while que:
        row, col = que.popleft()
        for l in range(4):
            nrow = row + drow[l] 
            ncol = col + dcol[l]
            if 0 <= nrow < R and 0 <= ncol < C and arr[nrow][ncol] != 1:
                arr[nrow][ncol] = 0


R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            arr[i][j] = 2 # 1초 지나도 아무 변화 X 1초부터 시작
        elif arr[i][j] == '.':
            arr[i][j] = 0  

for i in range(N-1): # 1초 부터 시작했기 때문 -1 
    time(i)
for i in arr: # 출력.....숫자로 계산해서 0인경우 . 이외의 경우 O 출력
    for j in i:
        if j == 0:
            j = '.'
        else:
            j = 'O'
        print(j, end = '')
    print()