import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, m, k = list(map(int, input().split()))
    live = [list(map(int, input().split())) for _ in range(n)]
    size = [[[-1, -1]]*(m+2*k) for _ in range(n+2*k)] # 세포가 확산 할 수 있는 최대의 크기로 설정
    for i in range(n):
        for j in range(m):
            size[k+i][k+j] = [live[i][j], 0]  # size의 중앙에 배치 확산 시키기 위해서 원래 가지고 있는 값, 시간 계산 값
    print(size)
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    cnt = k
    while cnt > 0: # k시간 동안 동작
        for r in range(n+2*k):
            for c in range(m+2*k):
                if size[r][c][0] == size[r][c][1] and size[r][c][0] != -1: #활성화 상태
                    for i in range(4):
                        new_r = r + dr[i]
                        new_c = c + dc[i]
                        if 0 <= new_r < m+2*k and 0 <= new_c < m+2*k and size[new_r][new_c][0] == -1:
                            size[new_r][new_c] = [size[r][c][0], 0]
                        elif 0 <= new_r < m+2*k and 0 <= new_c < m+2*k and size[new_r][new_c][1] == 0:
                            if size[new_r][new_c][0] < size[r][c][0]:
                                size[new_r][new_c][0] = size[r][c][0]
                elif size[r][c][0] > size[r][c][1]:
                    size[r][c][1] += 1
        cnt -= 1
    print(size)
