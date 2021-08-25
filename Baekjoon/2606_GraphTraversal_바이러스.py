from collections import deque


def bfs(S):
    que = deque()
    que.append(S)  # que에 초기값 저장
    visited[S] = 1  # 초기 1 컴 방문 설정

    while que:
        status = que.pop()
        for i in range(2, V + 1):  # 1컴 부터 시작
            if virus[status][i] == 1 and visited[i] == 0:  # network연결되어 있으면서 방문 안한 경우
                visited[i] = 1  # 방문으로 체크
                que.append(i)
    # print(visited)
    return sum(visited) - 1


V = int(input())  # 노드
E = int(input())  # network

virus = [[0] * (V + 1) for _ in range(V + 1)]  # 연결되어 있는 정보 확인 리스트
visited = [0] * (V + 1)

for _ in range(E):
    n1, n2 = map(int, input().split())
    virus[n1][n2] = 1
    virus[n2][n1] = 1

print(bfs(1))  # 초기 s = 1 com 이미 바이러스 걸림
