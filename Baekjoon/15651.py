import sys
sys.stdin = open('input.txt')

def dfs(n):
    if len(my_list) == m:
        print(*my_list)
    elif len(my_list) < m:
        for i in range(1, n+1): # 중복된거 제거해야하니까 num 부터 시작
            my_list.append(i)
            dfs(n) # 경우의수 맨 앞의 값 증가
            my_list.pop()

n, m = map(int, input().split())
my_list = []
dfs(n)