import sys
sys.stdin = open('input.txt')

n = int(input())
thesis = []
while True:
    thesis.append(input())
print(n, thesis)