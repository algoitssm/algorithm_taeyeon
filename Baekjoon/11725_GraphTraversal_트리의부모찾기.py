from collections import deque


def bfs(S):
    que = deque()
    que.append(S)  # que에 초기값 저장
    visited[S] = 1  # 초기 s = 1 루트 설정

    while que:
        status = que.pop()
        for i in range(1, V + 1):  # 1 부터 시작
            if adj[status][i] == 1 and visited[i] == 0:  # 연결되어 있으면서 방문 안한 경우
                visited[i] = 1  # 방문으로 체크
                que.append(i)
                print(i)
    return -1


V = int(input())  # 노드

adj = [[0] * (V + 1) for _ in range(V + 1)]  # 연결되어 있는 정보 확인 리스트
visited = [0] * (V + 1)

for _ in range(len(adj) - 2):
    n1, n2 = map(int, input().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1  # 연결 되어 있는 확인 리스트 생성

print(bfs(1))  # 초기 s = 1 루트 설정
