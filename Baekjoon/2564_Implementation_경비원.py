wid, leng = map(int, input().split())
num = int(input())
store = [list(map(int, input().split())) for _ in range(num)]
dong_place, dong_dis = map(int, input().split())
total = 0

for i in range(num):
    if dong_place == store[i][0]:
        total += abs(dong_dis - store[i][1])
    if dong_place == 1:
        if store[i][0] == 2:
            total += min(dong_dis + leng + store[i][1], wid + wid - dong_dis + leng - store[i][1])
        elif store[i][0] == 3:
            total += dong_dis + store[i][1]
        elif store[i][0] == 4:
            total += wid - dong_dis + store[i][1]
    elif dong_place == 2:
        if store[i][0] == 1:
            total += min(dong_dis + leng + store[i][1], wid + wid - dong_dis + leng - store[i][1])
        elif store[i][0] == 3:
            total += leng - store[i][1] + dong_dis
        elif store[i][0] == 4:
            total += leng - store[i][1] + wid - dong_dis
    elif dong_place == 3:
        if store[i][0] == 1:
            total += store[i][1] + dong_dis
        elif store[i][0] == 2:
            total += leng - dong_dis + store[i][1]
        elif store[i][0] == 4:
            total += min(wid + leng + leng - dong_dis - store[i][1], wid + dong_dis + store[i][1])
    elif dong_place == 4:
        if store[i][0] == 1:
            total += dong_dis + wid - store[i][1]
        elif store[i][0] == 2:
            total += leng - dong_dis + wid - store[i][1]
        elif store[i][0] == 3:
            total += min(wid + store[i][1] + dong_dis, wid + leng + leng - store[i][1] - dong_dis)

print(total)
