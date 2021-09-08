import sys

sys.setrecursionlimit(1000000)
sys.stdin = open("input.txt")


def solve(left, right):

    if left > right:
        return
    root = tree[left]  # 초기값 무조건 root
    idx = left + 1  # 루트 이외의 값들

    for i in range(idx, right + 1):  # 루트 + 1 부터 오른쪽 인덱스까지 읽어주면서
        if root < tree[i]:  # 루트와 비교하면서 idx다시 재설정
            idx = i
            break

    solve(left + 1, idx - 1)
    solve(idx, right)
    root_list.append(root)


tree = []
# 줄바꿈 입력 받기.........................................
while True:
    try:
        tree.append(int(input()))
    except:
        break
root_list = []

solve(0, len(tree) - 1)  # 인덱스
for i in root_list:
    print(i)
