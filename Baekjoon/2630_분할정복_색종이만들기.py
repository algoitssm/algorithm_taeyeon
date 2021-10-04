import sys
sys.stdin = open("input.txt")


def partition(paper):
    global b_cnt, w_cnt
    ltop = []
    rtop = []
    lbottom = []
    rbottom = []

    if color_solve(paper):
        if paper[0][0] == 1:  # 값이 1 이어서 blue인 경우 cnt += 1
            b_cnt += 1
        else:
            w_cnt += 1
    else: #네가지 방향으로 분리 필요
        mid = len(paper)//2
        for i in paper[:mid]:  # 절반 위에 상위 n//2
            ltop.append(i[:mid])
            rtop.append(i[mid:])

        for i in paper[mid:]:
            lbottom.append(i[:mid])
            rbottom.append(i[mid:])

        partition(ltop)
        partition(rtop)
        partition(lbottom)
        partition(rbottom)


def color_solve(paper_list):  # 모두 같은 색상으로 칠해져 있는가?
    temp = paper_list[0][0]
    for i in range(len(paper_list)):
        for j in range(len(paper_list)):
            if paper_list[i][j] != temp:
                return False  # 모두 같은 색이 아님
    return True # 모두 같은 색상임



n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
b_cnt = 0
w_cnt = 0

partition(paper)

print(w_cnt)
print(b_cnt)