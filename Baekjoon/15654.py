import sys
sys.stdin = open('input.txt')

def dfs(n):
    if len(my_list) == m:
        print(*my_list)
    elif len(my_list) < m:  # m 보다 작은 경우만 계속 같은 수 반복해도 되기때문에 조건문 필요
        for i in range(n):
            if my[i] not in my_list:
                my_list.append(my[i])
                dfs(n)
                my_list.pop()

n, m = map(int, input().split())
my = list(map(int, input().split()))
my.sort() # 오름차순 정렬하기위해서
my_list = []
dfs(n)