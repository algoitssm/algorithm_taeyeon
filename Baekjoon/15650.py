import sys
sys.stdin = open('input.txt')

def dfs(num):
    if len(my_list) == m:
        print(*my_list)
    for i in range(num, n+1): # 중복된거 제거해야하니까 num 부터 시작
        if i not in my_list:
            my_list.append(i)
            dfs(i+1) # 경우의수 맨 앞의 값 증가
            my_list.pop()

n, m = map(int, input().split())
my_list = []
dfs(1)
