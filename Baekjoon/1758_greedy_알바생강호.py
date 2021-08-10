nums = int(input())                           # 사람의 수 데이터 받아오기

my_list = []                                  # 사람들이 주려고 하는 tip을 담기 위한 리스트 생성
for num in range(nums):
    my_list.append(int(input()))              # tip 데이터를 받아들이고 리스트에 추가
# print(my_list)

my_list.sort(reverse=True)                    # 리스트를 내림차순으로 정렬
tips = 0                                      # 강호가 받는 처음 tip 을 0으로 설정
for my in range(len(my_list)):                # for문을 이용해 리스트 길이(사람의 수)만큼 반복
    tip = my_list[my] - (my + 1 - 1)          # tip = 원래생각한 돈 - (받은 등수 -1)
    if tip > 0:                               # 만일 tip < 0일 경우 받을 수 없기 때문에 양수의 경우만 판단 
        tips += tip
print(tips)