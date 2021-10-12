import sys
sys.stdin = open('input.txt')


for tc in range(int(input())):
    n, m, k = list(map(int, input().split()))
    cluster = [list(map(int, input().split())) for _ in range(k)]
    #print(cluster)
    for i in range(1, m+1): # 1초부터 m 초까지 이동
        live = [[0] * n for _ in range(n)]
        for r, c, num, dir in cluster:
            # 방향 상 하 좌 우 일때 행 열 변경
            if dir == 1:
                r -= 1
            elif dir == 2:
                r += 1
            elif dir == 3:
                c -= 1
            elif dir == 4:
                c += 1
            # 모서리에 도착하는 경우
            if r == 0 or r == n - 1 or c == 0 or c == n - 1:
                num //= 2
                if dir == 1 or dir == 3:
                    dir += 1
                else:
                    dir -= 1
            # 이동한 위치에 값이 없는 경우
            if not live[r][c]:
                live[r][c] = [num, dir, num] # 총합, 방향, 3개이상 한 곳에 모이는 곳을 대비해서 가장 큰 값
            # 이동한 위치에 이미 값이 존재하는 경우
            else:
                new_num = live[r][c][0] + num
                if num < live[r][c][2]: # 새롭게 들어온 미생물이 더 작은 경우
                    num = live[r][c][2]
                    dir = live[r][c][1]
                live[r][c] = [new_num, dir, num]
        cluster = []
        for i in range(n):
            for j in range(n):
                if live[i][j]:
                    cluster.append([i, j, live[i][j][0], live[i][j][1]])
    #print(live)
    result = 0
    for i in range(n):
        for j in range(n):
            if live[i][j]:
                result += live[i][j][0]
    print('#{} {}'.format(tc+1, result))