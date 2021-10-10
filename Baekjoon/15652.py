import sys
sys.stdin = open('input.txt')

def dfs(num):
    if len(my_list) == m:
        print(*my_list)
    elif len(my_list) < m:  # m 보다 작은 경우만 계속 같은 수 반복해도 되기때문에 조건문 필요
        for i in range(num, n+1): # 받은 num값 부터 시작
            my_list.append(i)
            dfs(i) # 변하는 i값을 dfs에 넣어줌 + 1씩 계속 증가
            my_list.pop()

n, m = map(int, input().split())
my_list = []
dfs(1)
