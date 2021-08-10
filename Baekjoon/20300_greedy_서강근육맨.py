machine = int(input())                                   # 기계 수 데이터 입력받기

loss = list(map(int, input().split()))                   # 근손실 값 리스트 생성, sort정렬
loss.sort()

my_list = []                                             # 최종적으로 2개, 1개의 기계를 사용하는 경우 발생하는 근손실의 값 넣을 수 있는 리스트 생성

for i in range(machine//2):                              # 기계수//2 만큼 반복
    if len(loss) % 2 == 0:                               # 주어지는 기계의 수가 짝수의 경우
        my_list.append(loss[i] + loss[- 1 - i])          # 맨 앞, 맨 뒤 반복하면서 두 값의 합
    else:                                                # 주어지는 기계의 수가 홀수의 경우
        my_list.append(loss[i] + loss[- 2 - i])          # 맨 앞, 뒤에서 두번째 값을 반복하면서 두 값의 합
    my_list.append(loss[-1])                             # 만들어진 리스트에 맨 뒤의 값을 추가

print(max(my_list))                                      # 만들어진 리스트에 max값을 출력