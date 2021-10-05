import sys
sys.stdin = open("input.txt")
# 시간 초과...how..

n = int(input())
x = '01101001'
while len(x) < n:
    for i in range(len(x)):
        if x[i] == '0':
            x += '1'
        else:
            x += '0'
print(x)
print(x[n])
