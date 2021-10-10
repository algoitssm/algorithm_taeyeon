import sys
sys.stdin = open('input.txt')

n = int(input())
for i in range(n):
    if i // 3 == 0:
        print(' '+'*'+' ')
    elif i // 3 == 1:
        print('* *')
    elif i// 3 == 2:
        print('***** ' * (n//3))''