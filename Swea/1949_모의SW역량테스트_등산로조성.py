import sys

sys.stdin = open("input.txt")


def solve(row, col, cnt):
    global result
    if result < max(sum(visited, [])):
        result = max(sum(visited, []))
    for i in range(4):
        nr = dr[i] + row
        nc = dc[i] + col
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if map_list[nr][nc] < map_list[row][col]:  # 새롭게 도착 지점이 더 작은 경우
                visited[nr][nc] = visited[row][col] + 1
                solve(nr, nc, cnt)
                visited[nr][nc] = 0
            else:
                if cnt == 1:  # 새롭게 도착 지점이 더 큰 경우인데 공사 가능한 경우
                    if map_list[nr][nc] - k < map_list[row][col]:  # 11 / 9 k =3 인 경우에 9-1 로 8만들어도됨
                        visited[nr][nc] = visited[row][col] + 1
                        temp = map_list[nr][nc]
                        map_list[nr][nc] = map_list[row][col] - 1  # 현재 위치에서 -1 해준다
                        solve(nr, nc, cnt - 1)
                        map_list[nr][nc] = temp
                        visited[nr][nc] = 0

    # return max(sum(visited, [])) # 이중 리스트 맥스 찾기


for tc in range(int(input())):
    n, k = map(int, input().split())
    map_list = [list(map(int, input().split())) for _ in range(n)]
    max_height = 0
    for i in range(n):
        for j in range(n):
            if max_height < map_list[i][j]:
                max_height = map_list[i][j]
    # print(max_height)
    max_height_list = []
    for i in range(n):
        for j in range(n):
            if map_list[i][j] == max_height:
                max_height_list.append([i, j])
    # print(max_height_list)

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    result = 0
    for map_height in max_height_list:
        visited = [[0] * n for _ in range(n)]
        visited[map_height[0]][map_height[1]] = 1  # 시작 방문 표현
        solve(map_height[0], map_height[1], 1)
    print("#{} {}".format(tc + 1, result))
