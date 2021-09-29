import sys

sys.stdin = open("input.txt")


pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1], # 우하좌상
    [0, 1, 0, 1], # 하상
    [1, 0, 1, 0], # 우좌
    [1, 0, 0, 1], # 우상
    [1, 1, 0, 0], # 우하
    [0, 1, 1, 0], # 하좌
    [0, 0, 1, 1], # 좌상
]

for tc in range(int(input())):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)] # 시간 누적

    dr = [0, 1, 0, -1] # 우하좌상 
    dc = [1, 0, -1, 0]

    stack = [(r, c)]
    visited[r][c] = 1

    result = 0
    while stack:
        r, c = stack.pop(0)
        result += 1 # 맨홀 뚜껑있는데도 위치할 수 있기에
        if visited[r][c] > l: # 시간 누적보다 주어진 시간이 큰경우 break
            break
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c

            if pipe[tunnel[r][c]][i] == 0: # pip연결 안된경우
                continue
            if nr < 0 or nr >= n or nc < 0 or nc >= m: # 새롭게 움직이는 경우 범위 안에 존재하는 경우에만 간응
                continue
            nd = (i + 2) % 4
            np = tunnel[nr][nc]

            if visited[nr][nc] or pipe[np][nd] == 0: # 방문안하고 pipe연결 안된 경우
                continue

            visited[nr][nc] = visited[r][c] + 1
            stack.append((nr, nc))


    print('#{} {}'.format(tc+1, result))






















