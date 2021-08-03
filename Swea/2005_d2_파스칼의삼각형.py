# 구글링의 도움...

T = int(input()) 
for t in range(1, T+1):
    num = int(input())
    print(f'#{t}') # test case 출력
    
    new_list = [] # 배열 생성 리스트
    for i in range(num):
        case = [] # 새로운 덧셈 배열 생성 리스트
        for j in range(i + 1):
            if j == 0 or i == j:
                case.append(1)
                print(1, end= ' ')
            else:
                case.append(new_list[i-1][j-1] + new_list[i-1][j]) 
                print(new_list[i-1][j-1] + new_list[i-1][j], end= ' ')
        new_list.append(case)
        print()


# 00
# 10 11
# 20 21 22
# 30 31 32 33
