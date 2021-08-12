city = int(input())

load = list(map(int,input().split()))
price = list(map(int, input().split()))

total = price[0] * load[0]                            # 초기 비용 -> 첫번째 지역을 벗어나기 위한 무조건 발생하는 비용
min_price = price[0]                                  # 첫 지역에서의 기름 비용을 최소비용으로 기준   
for i in range(1, city-1):                            # 마지막 지역의 기름가격과 정보는 필요x, 제외한 반복
    if price[i] >= min_price:                         # 1. 도착한 지점의 기름가격이 기준기름비용보다 큰 경우
        total += min_price * load[i]                  # 초기 비용 + (기준 비용 * 추가로 가야하는 길이)
    else:
        min_price = price[i]                          # 2. 도착한 지점의 기름가격이 기준기름비용보다 작은 경우
        total += min_price * load[i]                  # 초기 비용 + 기준 비용을 현재 위치의 기름 비용으로 설정하고 계산

# total += min_price * load[i]        
print(total)