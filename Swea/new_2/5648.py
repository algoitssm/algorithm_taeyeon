import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n = int(input())
    atom_list = []
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    atom_list = [(list(map(int, input().split()))) for _ in range(n)]
    for atom in atom_list:
        atom[0] *= 2 # 사이가 홀수인 경우에 문제
        atom[1] *= 2

    result = 0
    while len(atom_list) >= 2: # 충돌 할 원자 없을 때까지 1개 인경우 x
        for atom in atom_list: # 4가지 방향으로
            atom[0] += dr[atom[2]]
            atom[1] += dc[atom[2]]
        atom_list.sort(key=lambda x: (x[0], x[1])) # x좌표를 기준으로 같은값 찾음

        new = []
        i = 0
        while i < len(atom_list):
            if -2000 <= atom_list[i][0] <= 2000 and -2000 <= atom_list[i][1] <= 2000: # 이동한 지위치가 범위 안에 존재하는가
                if i < len(atom_list) - 1 and atom_list[i][0] == atom_list[i + 1][0] and atom_list[i][1] == atom_list[i + 1][1]: # x좌표를 기준으로 정렬을 했기 때문에 다음거랑 갑 비교
                    result += atom_list[i][3] # 현재 원자 에너지 결과에 더해준다
                    for j in range(1, len(atom_list) - i): # 같은 위치에 존재하는 원자 에너지 있는가 파악
                        if atom_list[i][0] == atom_list[i + j][0] and atom_list[i][1] == atom_list[i + j][1]:
                            result += atom_list[i + j][3] # 존재하면 에너지 결과 더해준다
                            flag = True
                        else:
                            flag = False # 같은 위치에 존재하는 원자 에너지 없음 break
                            break
                    if flag == False: # False인 경우에 인덱스 넘겨줘야하니까
                        i += j
                    else:
                        break
                else:
                    new.append(atom_list[i])  # 변경 된 위치로 반복 다시 돌리기 위해서 new리스트에 담는다
                    i += 1
            else:
                i += 1 # 범위 넘어가는 경우 인덱스 추가
        atom_list = new # 변경된 위치로 다시 반복 돌림
    print('#{} {}'.format(tc+1, result))
