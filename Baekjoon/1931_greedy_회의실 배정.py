num = int(input())
time_list = []
for i in range(num):
    start, finish = map(int, input().split())
    time_list.append((start, finish))

time_list.sort(key = lambda x: [x[1], x[0]])

room_count = 0
finish_time = 0
for time in time_list:
    if time[0] >= finish_time:
        finish_time = time[1]
        room_count += 1
print(room_count)