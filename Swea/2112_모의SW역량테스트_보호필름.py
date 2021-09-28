# testcase시간초과로 40개만 통과
import sys

sys.stdin = open("input.txt")


def pass_film(film):  # 필름 합격 여부 판단
    for i in range(w):  # 가로의 크기
        chk = False
        cnt = 1
        for j in range(d - 1):  # 필름의 두께
            if film[j][i] == film[j + 1][i]:  # 세로행 판단
                cnt += 1
                if cnt >= k:  # 합격기준 보다 같은 특성인 것이 큰 경우
                    chk = True
            else:
                cnt = 1
        if chk == False:
            return False
    return True


def solve(row, add, new_film):
    global max_v
    if row < d:
        if pass_film(new_film) == True:
            if add < max_v:
                max_v = add

        temp = [0] * d
        # print(temp)
        for i in range(d):
            temp[i] = new_film[i]

        solve(row + 1, add, temp)
        temp[row] = [0] * w
        solve(row + 1, add + 1, temp)
        temp[row] = [1] * w
        solve(row + 1, add + 1, temp)


for tc in range(int(input())):
    d, w, k = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(d)]

    if k == 1:  # k == 1인경우 무조건 통과
        result = 0
    max_v = 13
    solve(0, 0, film)  # 0번째 행에서 시작해서 add만큼
    result = max_v
