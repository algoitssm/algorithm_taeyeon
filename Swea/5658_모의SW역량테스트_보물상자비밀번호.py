import sys

sys.stdin = open("input.txt")

for tc in range(int(input())):
    N, K = map(int, input().split())
    num = list(map(str, input()))
    my_dic = [
        ("A", "10"),
        ("B", "11"),
        ("C", "12"),
        ("D", "13"),
        ("E", "14"),
        ("F", "15"),
    ]  # 가능한 16진수 리스트 생서
    new = []
    for i in range(0, N, N // 4):  # 4개의 방향으로 분리
        for j in range(N // 4):
            new.append(num[i + j : i + j + N // 4])
    # print(new)

    for j in range(1, (N // 4)):  # 맨뒤에 잘리는 경우에 나머지 요소 값 추가
        new[-j].extend(num[: N // 4 - j])
    # print(new)

    new_list = list(set(map(tuple, new)))  # set으로 중복 제거
    new_list = [list(i) for i in new_list]
    # print(new_list)
    for i in new_list:
        for j in range(len(i)):
            for k in range(len(my_dic)):
                if i[j] == my_dic[k][0]:
                    i[j] = my_dic[k][1]  # 알파벳 -> 숫자로 변경
    # print(new_list)

    result_list = []
    for i in new_list:
        result = 0
        for j in range(len(i)):
            result += int(i[j]) * (16 ** ((N // 4) - j - 1))
        result_list.append(result)
        result_list.sort(reverse=True)
    # print(result_list)
    print("#{} {}".format(tc + 1, result_list[K - 1]))
