import sys
sys.stdin = open('input.txt')

'''
# import itertools
# itertools 이용 permutations
n, m = map(int, input().split())
num = []
for i in range(1, n+1):
    num.append(str(i))
print(*list(map(' '.join, itertools.permutations(num, m))), sep='\n')
'''

def dfs(n):
    if len(my_list) == m:
        print(*my_list)
    for i in range(1, n+1):
        if i not in my_list:
            my_list.append(i)
            dfs(n)
            my_list.pop()

n, m = map(int, input().split())
my_list = []
dfs(n)