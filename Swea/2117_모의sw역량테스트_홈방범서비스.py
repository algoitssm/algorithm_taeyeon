import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, m = map(int, input().split())
    house_list = [list(map(int, input().split())) for _ in range(n)]

    house_place = [] # house가 위치하는 곳 담을 리스트
    for i in range(n):
        for j in range(n):
            if house_list[i][j] == 1:
                house_place.append((i, j))

    cnt_list = [] # 맵을 다 돌면서 house 개수 세기
    for i in range(n):
        for j in range(n):
            for k in range(1, n+2): # k가 1인 곳부터 n+2...? n홀수면 n+1 가능 짝수일 때
                cnt = 0
                for house in house_place:
                    if k > abs(house[0] - i) + abs(house[1] - j):  # k 를 기준으로 house와의 거리 계산
                        cnt += 1
                        cnt_list.append((cnt, k))
    result = 0
    for cnt_l in cnt_list: # cnt_list에 들어있는 cnt, k를 꺼내서 이익을 볼 수 있는지 판단 0 도 가능
        if m * cnt_l[0] - (cnt_l[1]**2 + (cnt_l[1]-1)**2) >= 0:
            if result < cnt_l[0]:
                result = cnt_l[0]
    print('#{} {}'.format(tc+1, result))
