from collections import deque


def bfs(S, K):
    visited[S] = 0
    que = deque()
    que.append(S)

    while que:
        hide = que.popleft()
        if hide == K:
            return visited[hide]
        if 0 <= hide * 2 < 100001 and visited[hide * 2] == -1:
            visited[hide * 2] = 1
            visited[hide * 2] = visited[hide]  # 방문 횟수 체크 동일
            que.appendleft(hide * 2)
        if 0 <= hide - 1 < 100001 and visited[hide - 1] == -1:
            visited[hide - 1] = 1
            visited[hide - 1] = visited[hide] + 1  # 방문 횟수 체크 + 1
            que.append(hide - 1)
        if 0 <= hide + 1 < 100001 and visited[hide + 1] == -1:
            visited[hide + 1] = 1
            visited[hide + 1] = visited[hide] + 1  # 방문 횟수 체크 + 1
            que.append(hide + 1)


N, K = map(int, input().split())
visited = [-1] * 100001

print(bfs(N, K))

"""from collections import deque


def bfs(N, K):
    que = deque()
    que.append(N)

    while que:
        hide = que.popleft()
        if hide == K:
            return cnt[hide]
        if 0 <= hide * 2 < 100001 and visited[hide * 2] == 0:  # 범위에 존재하면서 방문하지 않은 경우
            visited[hide * 2] = 1  # 방문 체크
            cnt[hide * 2] = cnt[hide]  # 방문 횟수 체크 동일
            que.append(hide * 2)
        if 0 <= hide - 1 < 100001 and visited[hide - 1] == 0:
            visited[hide - 1] = 1
            cnt[hide - 1] = cnt[hide] + 1  # 방문 횟수 체크 + 1
            que.append(hide - 1)
        if 0 <= hide + 1 < 100001 and visited[hide + 1] == 0:
            visited[hide + 1] = 1
            cnt[hide + 1] = cnt[hide] + 1  # 방문 횟수 체크 + 1
            que.append(hide + 1)


N, K = map(int, input().split())
visited = [0] * 100001
cnt = [0] * 100001

print(bfs(N, K))
"""
