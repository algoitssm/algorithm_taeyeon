import sys
sys.stdin = open('input.txt')

def solve(people_list, stairs_list):
    return 3
def solve(people_list, stairs_list):
    pass


def dfs(idx, people_list, stairs_list):
    global result
    if idx == len(stairs_dis):
        now_result = solve(people_list, stairs_list)
        if now_result < result:
            result = now_result
        return
    else:
        people_list.append(stairs_dis[idx][0]) # 계단 1번의 정보 넣는다
        stairs_list.append(1) # 계단 1번을 선택한 경우이기에
        dfs(idx+1, people_list, stairs_list)
        people_list.pop() # 되돌리기
        stairs_list.pop()

        people_list.append(stairs_dis[idx][1])
        stairs_list.append(2)  # 사다리를 2번을 선택한 경우이기에
        dfs(idx + 1, people_list, stairs_list)
        people_list.pop()
        stairs_list.pop()
        return



for tc in range(int(input())):
    n = int(input())
    people = [list(map(int, input().split())) for _ in range(n)]
    people_list = []
    stairs = []
    for i in range(n):
        for j in range(n):
            if people[i][j] == 1:
                people_list.append((i, j))
            elif people[i][j] != 0:
                stairs.append((i, j, people[i][j]))
    result = 100
    stairs_dis = [[0]*2 for _ in range(len(people_list))]
    for i in range(2):
        if i == 0:
            for j in range(len(people_list)):
                stairs_dis[j][0] += (abs(stairs[i][0] - people_list[j][0]) + abs(stairs[i][1] - people_list[j][1]))
        if i == 1:
            for j in range(len(people_list)):
                stairs_dis[j][1] += (abs(stairs[i][0] - people_list[j][0]) + abs(stairs[i][1] - people_list[j][1]))
    print(stairs_dis) # 왼쪽에 1번 계단 정보 2번 계단 정보와의 각 사람마다의 거리를 담는다 쥔짜 머리 터진다.
    people_list = [] # 사람과 사다리의 거리정보
    stairs_list = [] # 선택한 사다리 정보
    dfs(0, people_list, stairs_list)