import sys
sys.stdin = open("input.txt")


def solve(magnet_num, direction): # 자석 인덱스랑 , 방향 표현 1, -1
    direct_turn.append((magnet_num, direction))  # 돌아야 하는 자석들 포함
    visited[magnet_num][2] = 1
    visited[magnet_num][6] = 1
    left_magnet_num = magnet_num - 1 # 왼쪽 자석이랑 비교 (인덱스)
    right_magnet_num = magnet_num + 1 # 오른쪽 자석이랑 비교 (인덱스)
    if magnet_num == 0:  # 오른쪽만 반복 비교
        if magnet[magnet_num][2] != magnet[right_magnet_num][6] and not visited[right_magnet_num][6]:
            visited[right_magnet_num][6] = 1
            solve(right_magnet_num, direction*-1)
    elif magnet_num == 1 or magnet_num == 2: # 1, 2 양쪽 비교 필요한 자석
        if magnet[magnet_num][6] != magnet[left_magnet_num][2] and not visited[left_magnet_num][2]:
            visited[left_magnet_num][2] = 1
            solve(left_magnet_num, direction*-1)
        if magnet[magnet_num][2] != magnet[right_magnet_num][6] and not visited[right_magnet_num][6]:
            visited[right_magnet_num][6] = 1
            solve(right_magnet_num, direction * -1)
    elif magnet_num == 3:  # 왼쪽만 반복 비교
        if magnet[magnet_num][6] != magnet[left_magnet_num][2] and not visited[left_magnet_num][2]:
            visited[left_magnet_num][2] = 1
            solve(left_magnet_num, direction*-1)


def direction_turn(magnet_num, direction):
    if direction == 1:
        x = magnet[magnet_num].pop()
        magnet[magnet_num] = [x] + magnet[magnet_num]
    else:
        magnet[magnet_num] = magnet[magnet_num][1:] + [magnet[magnet_num][0]]


for tc in range(int(input())):
    k = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    turn_direction = [list(map(int, input().split())) for _ in range(k)] # 자석 번호, 방향 1 시계, -1 반시계

    for turn in turn_direction:
        visited = [[0] * 8 for _ in range(4)]  # 방문 여부 파악 turn별로 초기화 필요
        direct_turn = []
        solve(turn[0]-1, turn[1])  # 자석의 1,2,3,4 번호 중 한개(인덱스 접근 -1)와 방향 정보
        for direct in direct_turn:
            direction_turn(direct[0], direct[1])
        #print(direct_turn)

    cnt = 0
    #print(magnet)
    for i in range(4):
        if i == 0:
            if magnet[i][0] == 1:
                cnt += 1
        if i == 1:
            if magnet[i][0] == 1:
                cnt += 2
        if i == 2:
            if magnet[i][0] == 1:
                cnt += 4
        if i == 3:
            if magnet[i][0] == 1:
                cnt += 8
    print('#{} {}'.format(tc+1, cnt))