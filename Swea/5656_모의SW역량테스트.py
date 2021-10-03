import sys
import copy
from collections import deque
sys.stdin = open("input.txt")

def arrange_brick(brick): #존재하는 값 정렬하는 함수
    arr_brick = [[0]*w for _ in range(h)]
    for j in range(w): #한개의 열을 보기 위해서
        temp = []
        for i in range(h):
            if brick[i][j]: # 값이 존재한다면
                temp.append(brick[i][j])
        for k in range(len(temp)):
            arr_brick[h-len(temp)+k][j] = temp[k] # 전체 행의 높이중에서 - 존재하는 값을 빼고 + 인덱스 처리
    return arr_brick


def solve(brick, n): #맨 윗줄 읽고 벽돌 깨는 함수 몇개의 벽돌을 깰수 있나~~
    global cnt
    if n:
        for j in range(w):
            for i in range(h):
                if brick[i][j] != 0: # 첫번째 줄 0이 아닌것 시작
                    que = deque()
                    que.append((i, j, stand_brick[i][j]))
                    while que:
                        now_que = que.popleft()
                        if now_que[2] > 0:
                            brick[now_que[0]][now_que[1]] = 0
                            cnt += 1
                        for x in range(4): # 4가지 방향으로 벽돌 0으로 바꾸기 위해
                            for y in range(1, now_que[2]):# 벽돌 값을 기준으로..
                                nr = dr[x]*y + now_que[0]
                                nc = dc[x]*y + now_que[1]
                                if 0 <= nr < n and 0 <= nc < n and brick[nr][nc]:
                                    brick[nr][nc] = 0
                                    que.append((nr, nc, stand_brick[nr][nc]))
                    now_brick = arrange_brick(brick)
                n -= 1
    if not now_brick:
        return cnt



for tc in range(int(input())):
    n, w, h = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(h)]
    stand_brick = copy.deepcopy(brick)
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    cnt = 0
    solve(brick, n)
    print(cnt)