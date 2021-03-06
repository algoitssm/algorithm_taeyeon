def solve(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        print(preorder[0], end=" ")
        return

    root = preorder[0]
    root_idx = inorder.index(root)

    left_tree = inorder[:root_idx]  # 중위 순회의 루트 기준 왼쪽
    right_tree = inorder[root_idx + 1 :]  # 중위 순회의 루트 기준 오른쪽
    new_root_left = preorder[1 : 1 + root_idx]
    new_root_right = preorder[root_idx + 1 :]

    solve(new_root_left, left_tree)
    solve(new_root_right, right_tree)
    # return root
    print(root, end=" ")


T = int(input())
for tc in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    solve(preorder, inorder)
    print()
