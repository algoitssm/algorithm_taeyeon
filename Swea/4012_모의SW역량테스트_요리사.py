from itertools import combinations
import sys

sys.stdin = open("input.txt")


for tc in range(int(input())):
    num = [i for i in range(int(input()))]
    my_list = [list(map(int, input().split())) for _ in range(len(num))]
    max_v = []
    result_list = []
    for i in combinations(num, len(num) // 2):  # 요리를 할 수 있는 경우의 수 result_list에 추가
        result_list.append(i)
    for j in range(len(result_list) // 2):  # 경우의 수마다 나올수 있는 조합 {1,2,3}{4,5,6}의 경우 1,2 // 1,3 // 2,3
        s1 = []
        s2 = []
        for x, y in combinations(result_list[j], 2):  # 쌍방으로 ss1에 더하고{123}
            ss1 = my_list[x][y] + my_list[y][x]
            s1.append(ss1)
        for x, y in combinations(result_list[-j - 1], 2):  # j의 쌍에 맞는 {456}
            ss2 = my_list[x][y] + my_list[y][x]
            s2.append(ss2)
        ans = abs(sum(s1) - sum(s2))  # 절대값으로 두값의 차이
        max_v.append(ans)
    print("#{} {}".format(tc + 1, min(max_v)))  # 최솟값 출력
