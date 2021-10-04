import sys
sys.stdin = open("input.txt")

def solve(n):
    if n == 3:
        for i in range(3):
            if i == 0 or i == 2:
                star[i][:3] = ['*', '*', '*']
            elif i == 1:
                star[i][:3] = ['*', ' ', '*']
        return

    if n > 3:
        mid = n // 3
        for i in star[mid:mid*2]:
            for j in range(mid, 2*mid):
                i[j] = ' '
    n //= 3
    solve(n)
    for i in range(3):  # 3개로 분리 행
        for j in range(3):  # 3개로 분리 열
            if not (i == 1 and i == 1):
                for k in range(n):
                    star[n * i + k][n * j:n * j + n] = star[k][:n]  # 왼쪽 우상단이랑 같게 만듬



n = int(input())
m = n
star = [['*']* n for i in range(n)]
solve(n)
for i in star:
    for j in i:
        if j == '*':
            print('*', end ='')
        elif j == ' ':
            print(' ', end ='')
    print()

