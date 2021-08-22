import sys
from collections import deque

sys.stdin = open("input2.txt")


def union_move(row, col):
    union_list = []
    union_list.append([row, col])  # 연합 국가 포함해주는 리스트

    que = deque()
    que.append([row, col])
    # print(union_list)
    while len(que) > 0:  # 사라질 때 까지
        row, col = que.popleft()
        for i in range(4):
            nrow = row + drow[i]  # 새롭게 이동
            ncol = col + dcol[i]
            if 0 <= nrow < N and 0 <= ncol < N and visited[nrow][ncol] == 0:  # 방문하지 않은경우
                if L <= abs(country[nrow][ncol] - country[row][col]) <= R:
                    visited[nrow][ncol] = 1  # 방문했다고 표현
                    union_list.append([nrow, ncol])
                    que.append([nrow, ncol])
    return union_list


drow = [0, 0, 1, -1]
dcol = [1, -1, 0, 0]
N, L, R = map(int, input().split())
country = []
for _ in range(N):
    country.append(list(map(int, input().split())))
# print(country)

day = 0
while True:
    checked = False
    visited = [[0] * N for _ in range(N)]  # 방문 여부 파악
    for row in range(N):
        for col in range(N):
            if visited[row][col] == 0:
                visited[row][col] = 1  # 방문 하지 않았던 경우 방문으로 체크
                move = union_move(row, col)  # 연합국가 리스트 뽑아옴
                if len(move) >= 2:
                    checked = True
                    # day += 1           # 인구 이동할 예정으로 day+1
                    sum_union = sum(country[r][c] for r, c in move)
                    mean_union = sum_union // len(move)  # 연합리스트끼리 country에 해당하는 평균.
                    for r, c in move:
                        country[r][c] = mean_union  # 연합평균값으로 계산

    if checked == False:
        break
    day += 1
print(day)
