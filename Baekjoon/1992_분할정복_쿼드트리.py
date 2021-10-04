import sys
sys.stdin = open("input.txt")

# 2630 이랑 비슷하게 품

def partition(video):
    global result
    ltop = []
    rtop = []
    lbottom = []
    rbottom = []

    if color_solve(video):
        if video[0][0] == '1':  # 값이 1 이어서 blue인 경우 cnt += 1
            result.append(1)
        else:
            result.append(0)

    else: #네가지 방향으로 분리 필요
        mid = len(video)//2
        for i in video[:mid]:  # 절반 위에 상위 n//2
            ltop.append(i[:mid])
            rtop.append(i[mid:])

        for i in video[mid:]:
            lbottom.append(i[:mid])
            rbottom.append(i[mid:])
        result.append('(')
        partition(ltop)
        partition(rtop)
        partition(lbottom)
        partition(rbottom)
        result.append(')')


def color_solve(video_list):  # 모두 같은 색상으로 칠해져 있는가?
    temp = video_list[0][0]
    for i in range(len(video_list)):
        for j in range(len(video_list)):
            if video_list[i][j] != temp:
                return False  # 모두 같은 색이 아님
    return True # 모두 같은 색상임



n = int(input())
video = [str(input()) for _ in range(n)]
result = []
partition(video)
for i in range(len(result)):
    print(result[i], end ='')

