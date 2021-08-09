# tip = 원래생각한 돈 - (받은 등수 -1)
# tip < 0 받을 수 x

nums = int(input())

my_list = []

for num in range(nums):
    my_list.append(int(input()))
# print(my_list)

my_list.sort(reverse=True)
tips = 0
for my in range(len(my_list)):
    tips += my_list[my] - (my + 1 - 1)

print(tips)