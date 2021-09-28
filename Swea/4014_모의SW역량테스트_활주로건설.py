import sys

sys.stdin = open("input.txt")


def solve(road):
    visited = [0] * n
    slope = [True] * n  # slope 설치 가능 장소인지 파악
    for i in range(n - 1):
        if road[i] == road[i + 1]:  # 같은 값인 경우
            visited[i] = 1

        elif road[i] == road[i + 1] - 1:  # 오르막
            visited[i] = 1  # 방문표현
            cnt = 0
            for j in range(i, -1, -1):
                if road[i] == road[j] and slope[j]:
                    cnt += 1
                else:
                    break
            if cnt >= x:  # 같은 높이가 경사의 길이보다 긴 경우에 경사 설치 가능
                for j in range(i, i - x, -1):
                    visited[j] = 1  # 방문표현
                    slope[j] = False  # 현재 위치에는 더이상 경사 설치 불가
            else:
                return 0

        elif road[i] == road[i + 1] + 1:  # 내리막
            visited[i] = 1  # 방문표현
            cnt = 0
            for j in range(i + 1, n):
                if road[i + 1] == road[j] and slope[j]:
                    cnt += 1
                else:
                    break  # 이거 종료 조건 안하면 433433예시 문제...

            if cnt >= x:  # 같은 높이가 경사의 길이보다 긴 경우에 경사 설치 가능
                for j in range(i + 1, i + x):
                    visited[j] = 1  # 방문표현
                    slope[j] = False  # 현재 위치에는 더이상 경사 설치 불가
                    slope[i + x] = False
            else:
                return 0

    # print(visited)
    for k in range(n - 1):
        if not visited[k]:
            return 0
    return 1


for tc in range(int(input())):
    n, x = map(int, input().split())
    road_list = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for road in road_list:
        result += solve(road)
        # print(result)

    for road in zip(*road_list):
        result += solve(road)

    print("#{} {}".format(tc + 1, result))
