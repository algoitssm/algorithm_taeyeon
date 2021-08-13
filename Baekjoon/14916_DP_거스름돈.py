money = int(input())

# 5로 나눈 나머지 돈의 값
remain_money = money % 5
# 주어진 돈이 1이거나 3인경우 (5이하의 값중에 2로 나눌 수 없는 예외 값)
if money == 1 or money == 3:
    count = -1
# 나머지가 짝수의 경우 몫만 더해준다    
elif remain_money % 2 == 0:
    count = money // 5 + remain_money // 2
# 나머지가 홀수인 경우 
else:
    count = (money // 5) + ((remain_money + 5) // 2) - 1
print(count)
