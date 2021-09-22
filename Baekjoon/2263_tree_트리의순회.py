# 18 % 메모리 초과

import sys

sys.stdin = open("input.txt")

# 인덱스로 탐색필요
def solve(posterorder, inorder):
    if len(posterorder) == 0:
        return

    print(posterorder[-1], end=" ")  # posterorder의 맨 뒤 root를 출력
    idx = inorder.index(posterorder[-1])

    solve(posterorder[:idx], inorder[:idx])  # 루트 기준으로 inorder분리, 맨뒤에 위치하는 루트를 제외한 분리
    solve(posterorder[idx:-1], inorder[idx + 1 :])


n = int(input())
inorder = list(map(int, input().split()))
posterorder = list(map(int, input().split()))
solve(posterorder, inorder)
print()
