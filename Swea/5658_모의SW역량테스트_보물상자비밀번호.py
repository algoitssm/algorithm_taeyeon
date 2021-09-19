import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N, K = map(int, input().split())
    num = list(map(str, input()))
    my_dic = [('A', '10'), ('B', '11'), ('C', '12'), ('D', '13'), ('E', '14'), ('F', '15')]
    new = []
    for i in range(0, N, N // 4):
        for j in range(N//4):
            new.append(num[i+j:i+j+N//4])
    #print(new)

    for j in range(1, (N//4)):
        new[-j].extend(num[:N//4-j])


    new_list = list(set(map(tuple, new)))
    new_list = [list(i) for i in new_list]
    #print(new_list)
    for i in new_list:
        for j in range(len(i)):
            for k in range(len(my_dic)):
                if i[j] == my_dic[k][0]:
                    i[j] = my_dic[k][1]
    #print(new_list)

    result_list = []
    for i in new_list:
        result = 0
        for j in range(len(i)):
            result += int(i[j]) * (16 ** ((N//4)-j-1))
        result_list.append(result)
        result_list.sort(reverse=True)
    #print(result_list)
    print('#{} {}'.format(tc+1, result_list[K-1]))


