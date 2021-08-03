T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())

    new_list = []
    for n in range(N):
        new_list.append(list(map(int, input().split())))

# print(new_list)

    max_value = 0
    for i in range(N-M+1):
        # M:2인경우 0,1합했을 때, 5가지 경우가 나와야 하므로 최대 4
        for ii in range(N-M+1):

            total = 0
            for j in range(M):
                for jj in range(M):
                    total += new_list[i+j][ii+jj]
            if total > max_value:
                max_value = total

    print(f'#{t} {max_value}')
