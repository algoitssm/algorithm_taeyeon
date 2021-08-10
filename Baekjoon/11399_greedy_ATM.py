nums = int(input())                              # 사람의 수 데이터 불러오기

person = list(map(int, input().split()))         # 사람 마다 기다리는 시간 데이터 불러오기, sort정렬
person.sort()

total = 0                                        # 사람마다 배열해서 기다리는 시간 
total_list= []                                   # 기다리는 시간을 넣을 수 있는 리스트 생성
# print(person)
for num in range(nums):                          # 사람의 수만큼 반복
    total += person[num]                         # 기다리는 시간을 순서별로 합, 1번째 1, 2번째 1+2, 3번째 1+2+3 ...
    total_list.append(total)
print(sum(total_list))
    