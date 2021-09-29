import sys

sys.stdin = open("input.txt")


for tc in range(int(input())):
    n, m, c = map(int, input().split())
    honey_list = [list(map(int, input().split())) for _ in range(n)]
    print(honey_list)

    # 같은 줄에 꿀통 위치하는 경우 j값이 +m
    # 다른 줄인 경우 무조건 가능
    # 최대한 많은 양을 담기위한 제곱
    first_honey_list = []
    second_honey_list = []
    for i in range(n):
        for j in range(n - m + 1):  # 가능한 열의 값 n :4 개면 m: 2개고 + 1 인덱스니까
            max_honey_1 = 0

            for k in range(i + 1, n):  # 두번째 사람인데 행이 다를 때 자유롭게
                second_person = honey_list[k][j : j + m]
                # print(second_person)
                max_honey_2 = 0
                if sum(second_person) <= c:
                    for p in second_person:
                        max_honey_2 += p ** 2
                elif sum(second_person) > c: # 경우의수....................................................
                    if max_honey_2 < (max(second_person)) ** 2:
                        max_honey_2 = (max(second_person)) ** 2
                second_honey_list.append(max_honey_2)

            for k in range(j + m, n - m + 1):  # 두번째 사람인데 행이 같은 경우
                second_person = honey_list[i][k : k + m]
                # print(second_person)
                max_honey_2 = 0
                if sum(second_person) <= c:
                    for p in second_person:
                        max_honey_2 += p ** 2
                elif sum(second_person) > c:
                    if max_honey_2 < (max(second_person)) ** 2:
                        max_honey_2 = (max(second_person)) ** 2
                second_honey_list.append(max_honey_2)

        first_person = honey_list[i][j : j + m]  # 첫번째 사람의 경우

    print(first_honey_list)
    # print(second_honey_list)
