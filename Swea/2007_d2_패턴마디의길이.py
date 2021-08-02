T = int(input())
for t in range(1, T+1):
    word = input()
    for i in range(1, 10):
        if word[:i] == word[i:2*i]:
            print(f'#{t} {i}')
            break