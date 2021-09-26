import sys

sys.stdin = open("input.txt")


def solve(cost, m):
    global min_cost

    if m > 11:
        if min_cost > cost:
            min_cost = cost
        return

    solve(cost + one_day * month[m], m + 1)

    solve(cost + one_month, m + 1)

    solve(cost + three_month, m + 3)


for tc in range(int(input())):
    one_day, one_month, three_month, one_year = map(int, input().split())
    month = list(map(int, input().split()))
    # print(month)
    min_cost = one_year
    solve(0, 0)  # 0원에서 시작하고 1월부터 계산
    print("#{} {}".format(tc + 1, min_cost))
