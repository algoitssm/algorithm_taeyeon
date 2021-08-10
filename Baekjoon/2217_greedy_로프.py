nums = int(input())                        # 로프의 개수데이터 받아오기

my_list = []                               # 로프가 들어올릴 수 있는 무게 리스트 생성
for num in range(nums):
    my_list.append(int(input()))

my_list.sort(reverse=True)                 # 로프가 들어올릴 수 있는 무게 내림차순으로 정렬(최대로 들어올릴 수 있는 무게를 찾아야 하기 때문에)

total = []                                 # 들어올릴 수 있는 무게의 경우의 수를 넣을 수 있는 리스트 생성 
for j in range(nums):                      # 큰 수를 기준으로 정렬한 my_list에서 하나씩 로프를 한개씩 추가하면서 무게 측정
    total.append(my_list[j] * (j+1))

print(max(total))