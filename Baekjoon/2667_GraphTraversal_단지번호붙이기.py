import sys
sys.stdin = open('input.txt')

def dfs(row, col):
    global cnt
    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]
    arr[row][col] = 1000 # 방문 25**2 표현
    cnt += 1 # 연결 개수 판단
    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if 0 <= nrow < N and 0 <= ncol < N and arr[nrow][ncol] == 1:
            dfs(nrow, ncol)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)

result = []
for i in range(N):
    for j in range(N):
        cnt = 0 # 1찾을 때마다 초기화
        if arr[i][j] == 1:
            dfs(i, j)
            result.append(cnt)
result.sort()
print(len(result), *result, sep='\n')  # 집단 개수, 한 줄에 한개 씩 출력