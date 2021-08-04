grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
T = int(input())
for t in range(1, T+1):
    number, num = map(int, input().split())
    total = []
    for n in range(1, number+1):
        x, y, z = map(int, input().split())
        total.append(round(x * 0.35 + y * 0.45 + z * 0.2))

    num_socre = total[num-1]
    #점수가 높은순으로 배열
    total.sort(reverse=True)

    # total 리스트에 몇번째에 위치해 있는지 // 인원수 비율
    rank_total = total.index(num_socre) // (number//10) 

    # grades 리스트 값
    garde_num = grades[rank_total]
    print(f'#{t} {garde_num}')