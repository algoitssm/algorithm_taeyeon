import sys
sys.stdin = open('input.txt')


def dfs(num):
    if len(my_list) == m:
        print(*my_list)
    elif len(my_list) < m:  # m 보다 작은 경우만 계속 같은 수 반복해도 되기때문에 조건문 필요
        for i in range(num, n): # (0 인덱스 시작) num 기준으로 중복 된 값 제거해주기
            if my[i] not in my_list:
                my_list.append(my[i])
                dfs(i) # for문 돌면서 자동으로 +1
                my_list.pop()

n, m = map(int, input().split())
my = list(map(int, input().split()))
my.sort() # 오름차순 정렬하기위해서
my_list = []
dfs(0)