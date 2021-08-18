small, big = map(int, input().split())

cnt = 1
while True:
    if small == big:  # 5,5 인경우 밑에서 걸러져버림
        break
    # 짝수가 아니면서 마지막 자리가 1이 아닌경우 & 최종값보다 주어진값이 작은경우
    elif small > big or ((big % 2 != 0) and (big % 10 != 1)):
        cnt = -1
        break
    elif small < big:  # 기본
        if big % 2 == 0:  # 짝수
            big = big // 2  # 2나눈 몫
            cnt += 1

        elif big % 2:  # 홀수
            big = big // 10  # 10으로나눈 몫
            cnt += 1

print(cnt)

# deque

"""
cnt = 1
while big != small:
    if big < small:
        count = -1
        break

    if (big % 2) == 0:
        if (big % 2) == 0:
            big = big // 2
            cnt += 1

    else:
        big = big // 10
        cnt += 1
"""
