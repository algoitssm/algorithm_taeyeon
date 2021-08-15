num = int(input())
drink = list(map(int, input().split()))

drink.sort(reverse=True)
drink_min = drink[0]
# 10 9 6 3 2
total = 0
for i in range(1, len(drink)):
    drink_min = drink_min + (drink[i] / 2)
print(drink_min)
