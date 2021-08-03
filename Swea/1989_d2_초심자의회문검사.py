T = int(input())

for t in range(1, T+1):
    word = input()
    for wo in range((len(word))//2):
        # word길이의 절반만금까지만 반복
        if word[wo] != word[-1-wo]:
            # 앞뒤가 다른경우 0
            result = 0
        else:
            result = 1

    print(f'#{t} {result}')