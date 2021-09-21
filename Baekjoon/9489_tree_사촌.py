import sys

sys.stdin = open("input.txt")


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:  # 0, 0 받은 경우 break
        break
    tree = list(map(int, input().split()))

    parents = [-1 for i in range(len(tree))]  # -1로 채운 부모 인덱스 담을 리스트 생성
    root = parents[0]
    cousin = tree.index(b)  # b 위치 찾기
    for i in range(1, len(tree)):
        if tree[i] != tree[i - 1] + 1:  # 연속된 값인지 확인
            root += 1
        parents[i] = root  # 연속된 값인 경우 같은 값을 인덱스에 입력
    # print(parents, cousin)

    result = 0
    for i in range(1, len(tree)):
        if parents[i] != parents[cousin]:  # 부모가 다른경우
            # print(i)
            if parents[parents[i]] == parents[parents[cousin]]:  # 할아버지가 같은 경우
                result += 1
                # print(i)
    print(result)
