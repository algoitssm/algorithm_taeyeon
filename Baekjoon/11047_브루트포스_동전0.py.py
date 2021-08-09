num, total = map(int,input().split())
money_list = []
for i in range(num):
    money = int(input())
    money_list.append(money)

coin_count = 0
for n in range(1, num+1):
    if total >= money_list[-n]:
        coin_count += total//money_list[-n]
        total = total % money_list[-n]

print(coin_count)