N = int(input())
tree = {}
for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]
    # print(tree) A B C = > {'A': ['B', 'C']}

# 전위 순회 : 루트/왼쪽/오른쪽
def preorder(root):
    if root != ".":  # 값이 존재하는 경우
        left = tree[root][0]
        right = tree[root][1]
        print(root, end="")
        preorder(left)
        preorder(right)


# 중위 순회 : 왼쪽/루트/오른쪽
def inorder(root):
    if root != ".":  # 값이 존재하는 경우
        left = tree[root][0]
        right = tree[root][1]
        inorder(left)
        print(root, end="")
        inorder(right)


# 후위 순회 : 왼쪽/오른쪽/루트
def postorder(root):
    if root != ".":  # 값이 존재하는 경우
        left = tree[root][0]
        right = tree[root][1]
        postorder(left)
        postorder(right)
        print(root, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
print()
