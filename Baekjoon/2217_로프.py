nums = int(input())

my_list = []

for num in range(nums):
    my_list.append(int(input()))

my_list.sort(reverse=True)

total = []
# 큰 수를 기준으로 정렬한 list에서 하나씩 로프 추가하면서 무게 측정
for j in range(nums):
    total.append(my_list[j] * (j+1))

print(max(total))