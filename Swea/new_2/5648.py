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
    while len(atom_list) >= 2:
        for atom in atom_list:
            atom[0] += dr[atom[2]]
            atom[1] += dc[atom[2]]
        atom_list.sort(key=lambda x: (x[0], x[1])) # x좌표를 기준으로 같은값 찾음

        new = []
        i = 0
        while i < len(atom_list):
            if -2000 <= atom_list[i][0] <= 2000 and -2000 <= atom_list[i][1] <= 2000:
                if i < len(atom_list) - 1 and atom_list[i][0] == atom_list[i + 1][0] and atom_list[i][1] == atom_list[i + 1][1]:
                    result += atom_list[i][3]
                    for j in range(1, len(atom_list) - i):
                        if atom_list[i][0] == atom_list[i + j][0] and atom_list[i][1] == atom_list[i + j][1]:
                            result += atom_list[i + j][3]
                            flag = True
                        else:
                            flag = False
                            break
                    if flag == False:
                        i += j
                    else:
                        break
                else:
                    new.append(atom_list[i])
                    i += 1
            else:
                i += 1 # 범위 넘어가는 경우 인덱스 추가
        atom_list = new
    print('#{} {}'.format(tc+1, result))
