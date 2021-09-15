import sys
sys.stdin = open('input.txt')
"""
def solve(t, k):
    if t == 1:
        if len(tree[k]) == 1:
            return False
        else:
            return True
    elif t == 2: # 무조건 true
        return True
"""
# 시간초과...
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
# print(tree)
q = int(input())
for i in range(q):
    t, k = map(int, sys.stdin.readline().split())
    if t == 1: # 단절점의 경우
        if len(tree[k]) > 1: # 연결노드가 1개 이상인 경우에 yes
            result = 'yes'
        else:
            result = 'no'
    else: # 단절선인 경우 무조건 true
        result = 'yes'
    print(result)