import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, m, k = list(map(int, input().split()))
    cluster = [list(map(int, input().split())) for _ in range(k)]
    visited = [[0]*k for _ in range(k)]
    direction = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if i == 0 or j == 0 or i == k-1 or j == k-1:
                visited[i][j] = -1  # 약품을 칠한 경우 방문 표현으로 해줌

    for i in range(1, m):
        for r, c, num, dir in cluster:
            if not visited[r][c]:
                if dir == 1:
                    r -= 1
                elif dir == 2:
                    r += 1
                elif dir == 3:
                    c -= 1
                elif dir == 4:
                    c += 1
                visited[r][c] = num
                direction[r][c] = dir
            elif visited[r][c] == -1:
                num //= 2
                if dir == 1 or dir == 3:
                    dir += 1
                else:
                    dir -= 1
            else:
                if visited[r][c] < num:
                    num += visited[r][c]
                else:
                    num += visited
                    dir = direction[r][c]
    print(cluster)

