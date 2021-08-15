""" 시간 초과 코드!!! heapq
cnt = int(input())

class_time = []
for _ in range(cnt):
    start, end = map(int, input().split())
    class_time.append((start, end))

class_time.sort(key=lambda x: [x[0], x[1]])

cnt = [0]
for time in class_time:
    if time[0] >= min(cnt):
        cnt.remove(min(cnt))
        cnt.append(time[1])
    else:
        cnt.append(time[1])
print(len(cnt))

"""

import heapq
import sys

cnt = int(input())

class_time = []
for _ in range(cnt):
    start, end = map(int, sys.stdin.readline().split())
    class_time.append((start, end))

class_time.sort(key=lambda x: [x[0], x[1]])

cnt = [0]
for time in class_time:
    if time[0] >= cnt[0]:
        heapq.heappop(cnt)
        heapq.heappush(cnt, time[1])
    else:
        heapq.heappush(cnt, time[1])

print(len(cnt))
