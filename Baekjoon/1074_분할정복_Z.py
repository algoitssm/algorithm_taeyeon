import sys

sys.stdin = open("input.txt")

n, r ,c = map(int, input().split())

result = 0
while n > 0:
    if n == 1:
        if r == 0 and c == 1:
            result += 1
        elif r == 1 and c == 0:
            result += 2
        elif r == 1 and c == 1:
            result += 3
    elif n > 1:
        mid = (2 ** n) // 2  # 범위의 중간
        if r >= mid and c < mid:  # 왼쪽 아래
            result += (mid ** 2)*2  # mid를 기준으로 mid**2이 박스 크기
            r -= mid
        elif r >= mid and c >= mid:  # 오른족 아래
            result += (mid ** 2)*3
            c -= mid
            r -= mid
        elif r < mid and c >= mid:  # 오른쪽 위
            result += (mid ** 2)
            c -= mid
    n -= 1
print(result)