math_ex = input().split("-")


start = 0

# 첫시작은 + 이고, 이후 +인 경우 해당 55 + 50
for math in math_ex[0].split("+"):
    start += int(math)
# print(start)

# -인 경우
for my in range(1, len(math_ex)):
    for my_2 in math_ex[my].split("+"):
        start -= int(my_2)
print(start)
