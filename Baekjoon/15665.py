import sys
sys.stdin = open('input.txt')


def dfs(n):
    if len(my_list) == m:
        print(*my_list)
    elif len(my_list) < m:  # m 보다 작은 경우만 계속 같은 수 반복해도 되기때문에 조건문 필요
        check = -1 #  같은 수 반복 안할 수 있도록 체크 포인트 필요
        for i in range(n):
            if my[i] != check: # 방금 쓴 수가 같은 수인가 파악 필요
                my_list.append(my[i])
                check = my[i]
                dfs(n) # for 문 돌면서 i 값 변경되는 것부터 10 번째 줄 코드 돈다
                my_list.pop()

n, m = map(int, input().split())
my = list(map(int, input().split()))
my.sort() # 오름차순 정렬하기위해서
# visited = [0]*n # 방문 체크 필요x
my_list = []
dfs(n)
