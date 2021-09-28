from itertools import permutations
import sys
import math

sys.stdin = open("input.txt")

"""
def solve(my_final_list, pos):
    global result_final, min_value, max_value
    operate = ['+', '-', '*', '/']

    if len(my_final_list) < 3:
        return
    elif len(my_final_list) == 3:
        temp = my_final_list[0] + my_final_list[1] + my_final_list[2]
        temp = round(eval(temp))
        if min_value > temp:
            min_value = temp
        if max_value < temp:
            max_value = temp
        print(max_value - min_value)


    if pos + 1 < len(my_final_list):
        if my_final_list[1] in operate:
            temp = my_final_list[0] + my_final_list[1] + my_final_list[2]
            temp = str(math.trunc(eval(temp)))
            my_final_list = [temp] + my_final_list[3:]
            solve(my_final_list, pos+1)


for tc in range(int(input())):
    n = int(input())
    operator = list(map(int, input().split()))
    num = list(map(str, input().split()))
    oper = []
    for i in range(4):
        if i == 0:
            oper += ['+']*operator[0]
        if i == 1:
            oper += ['-']*operator[1]
        if i == 2:
            oper += ['*']*operator[2]
        if i == 3:
            oper += ['/']*operator[3]
    results = []
    result = []
    permutations_list = list(permutations(oper))
    permutations_list = list(set(permutations_list))
    # print(permutations_list)
    for my_list in permutations_list:
        for i in range(len(num)-1):
            result += num[i] + my_list[i]
    # print(result)
    final = []
    for re in range(0, len(result), len(oper)*2):
        final.append(result[re:re+len(oper)*2])
    # print(final)
    for i in range(len(final)):
        plus = num[-1]
        final[i] += plus
        # final[i] = ''.join(final[i])
    # print(final)

    result_final = 0
    min_value = 10000000
    max_value = 0
    for fi in final:
        solve(fi, 0)
"""


def solve(idx, result):
    global min_result, max_result
    if idx == n - 1:
        if result < min_result:  # 최소 값 변경
            min_result = result
        if result > max_result:  # 최대 값 변경
            max_result = result
        return max_result - min_result

    for i in range(4):
        if operator[i]:  # 연산자 존재하는 경우,
            if i == 0:
                operator[i] -= 1
                solve(idx + 1, result + num[idx + 1])
                operator[i] += 1
            elif i == 1:
                operator[i] -= 1
                solve(idx + 1, result - num[idx + 1])
                operator[i] += 1
            elif i == 2:
                operator[i] -= 1
                solve(idx + 1, result * num[idx + 1])
                operator[i] += 1
            elif i == 3:
                operator[i] -= 1
                solve(idx + 1, int(result / num[idx + 1]))
                operator[i] += 1


for tc in range(int(input())):
    n = int(input())
    operator = list(map(int, input().split()))
    num = list(map(int, input().split()))
    # print(num, operator)
    min_result = 100000000
    max_result = -100000000
    solve(0, num[0])
    print("#{} {}".format(tc + 1, max_result - min_result))
