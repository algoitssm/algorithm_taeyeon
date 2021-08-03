T = int(input())
for t in range(1, T+1):
    num = list(map(int, input().split()))
    
    nums = sorted(num)
    num_sort = nums[1:9]
    sum_total = sum(num_sort)
    # 정수 값만을 출력
    mean_total = round(sum_total/8)

    print(f'#{t} {mean_total}')