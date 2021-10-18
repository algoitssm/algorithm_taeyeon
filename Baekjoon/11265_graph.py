import sys
sys.stdin = open('input.txt')

# 플로이드–와샬?
n, m = map(int, input().split())
time = [list(map(int, input().split())) for _ in range(n)]
party_room = [list(map(int, input().split())) for _ in range(m)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if time[i][j] > time[i][k] + time[k][j]:
                time[i][j] = time[i][k] + time[k][j]
for party in party_room:
    if time[party[0]-1][party[1]-1] <= party[2]:
        print('Enjoy other party')
    else:
        print('Stay here')