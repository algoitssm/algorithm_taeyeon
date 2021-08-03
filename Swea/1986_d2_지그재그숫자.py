T = int(input())

for t in range(1, T+1):
    num = int(input())
    total = 1
    for n in range(2, num+1):
        if n % 2 == 1:
            total += n
        else:
            total -= n

    print(f'#{t} {total}')