from collections import deque


def bfs(root):
    node = []
    visited[root] = 1  # 방문 표현3
    que = deque()
    que.append(root)
    while que:
        water = que.popleft()
        # print(visited[tree[water][0]]) root 읽는게 아니라 인덱스
        if visited[tree[water][0]] == 1 and len(tree[water]) == 1:  # 연결노드 부모 한개이고 tree와 연결 되어 있는 경우
            node.append(water)
        for i in tree[water]:
            if visited[i] == 0:
                visited[i] = 1
                que.append(i)

    return node


N, W = map(int, input().split())
tree = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)  # 노드 방문여부
for _ in range(N - 1):
    n1, n2 = list(map(int, input().split()))
    tree[n1].append(n2)
    tree[n2].append(n1)  # tree 연결 노드 생성
# for i in tree:
#    if len(i) == 1:
#        node += 1

print(tree)
print(bfs(1))


# enumerate 사용해서 부모노드 제외하공
