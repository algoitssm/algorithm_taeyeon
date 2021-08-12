n = int(input())

my_price = []
for i in range(n):
    my_price.append(int(input()))
my_price.sort(reverse=True)

price = 0
for my in range(2, len(my_price), 3):
    price += my_price[my]
print(sum(my_price) - price)

# 1 2 (3) 4 5 (6) 9 10
# 2 (3) 4 5 (6) 9 10
# (3) 4 5 (6) 9 10

# 10 9 (8) 7 6 (5) 4 3
# 10 9 (8) 7 6 (5) 4
# 10 9 (8) 7 6 (5)
