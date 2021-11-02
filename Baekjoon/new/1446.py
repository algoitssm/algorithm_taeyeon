import sys
sys.stdin = open("input.txt")


n, d = map(int, input().split())
load_list = [list(map(int, input().split())) for _ in range(n)]

graph = [[] for _ in range(1001)]
dis = [i for i in range(d+1)]
for load in load_list:
    graph[load[0]].append([load[1], load[2]])
for i in range(d+1): # 모든 간선 정보를 판단
    if dis[i-1] + 1 < dis[i]: # 기존에 가지고 있는 최소 거리보다 큰 경우
        dis[i] = dis[i-1] + 1 # 값 변경
    for end, load in graph[i]: # 하나씩 읽어들이면서 판단
        if end <= d and load + dis[i] < dis[end]: # 현재 위치한 곳의 값 + load 가 더 작은경우 값 변경
            dis[end] = load + dis[i]
print(dis[d])

