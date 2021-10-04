import sys

sys.stdin = open("input.txt")



n = int(input())
video = [list(map(int, input().split())) for _ in range(n)]
print(video)
for i in range(n):
    for j in range(n):
        while n > 0:
            mid = n // 2
            if i < mid and j < mid:  # 왼쪽 위
                video[:mid][j]
            elif i < mid and j >= mid:  # 오른쪽 위
            elif i >= mid and j < mid: #왼쪽 아래
            elif i >= mid and j >= mid: # 오른쪽 아래