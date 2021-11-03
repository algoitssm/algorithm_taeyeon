import sys
sys.stdin = open("input.txt")

nmr = list(map(int, input().split()))
items = list(map(int, input().split()))
area_list = [list(map(int, input().split())) for _ in range(nmr[2])]
graph = [[999999 for _ in range(nmr[0])] for _ in range(nmr[0])]

for area in area_list: # 행렬생성
    graph[area[0] - 1][area[1] - 1] = area[2]
    graph[area[1] - 1][area[0] - 1] = area[2]
result = []
for k in range(nmr[0]):
    for i in range(nmr[0]):
        for j in range(nmr[0]):
            if i == j:
                continue # graph[i][j] = 0
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]  #거리의 길이를 최단으로 설정

total = 0
for i in range(nmr[0]): # 행을 기준으로 합산
    now_result = 0
    for j in range(nmr[0]):
        if graph[i][j] <= nmr[1]: # 기준 길이보다 작은 경우에
            now_result += items[j] # 아이템 수 더해주고
    now_result += items[i] # 현재 행의 아이템 수를 더해준다(떨어진 위치)
    if now_result > total:
        total = now_result
print(total)