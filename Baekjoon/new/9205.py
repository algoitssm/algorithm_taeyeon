import sys
sys.stdin = open("input.txt")


t = int(input())
for tc in range(t):
    n = int(input()) # 편의점 개수
    rock_list = [list(map(int, input().split())) for _ in range(n+2)]
    graph = [[9999999 for _ in range(n+2)] for _ in range(n+2)]

    for i in range(n+2):
        for j in range(n+2):
            if i == j:
                continue
            elif abs(rock_list[i][0] - rock_list[j][0]) + abs(rock_list[i][1] - rock_list[j][1]) <= 1000:
                graph[i][j] = 1 # 이동이 가능함을 표현 [[9999999, 1, 9999999, 9999999], [1, 9999999, 1, 9999999], [9999999, 1, 9999999, 1], [9999999, 9999999, 1, 9999999]]

    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if i == j:
                    continue
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j] #최단거리로 설정 [[9999999, 1, 2, 3], [1, 9999999, 1, 2], [2, 1, 9999999, 1], [3, 2, 1, 9999999]]
    if graph[0][-1] != 9999999:
        print('happy')
    else:
        print('sad')

