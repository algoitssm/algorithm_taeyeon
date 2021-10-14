import sys
sys.stdin = open('input.txt')

#
n = int(input())
star = ["  *  ", " * * ", "*****"]
n_list = [3*(2**i) for i in range(11)]
# print(n_list) # [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072]
# print(pow)
k = n_list.index(n)
for _ in range(k):
    c = []
    for i in range(len(star)*2):
        m = len(star)
        if i < m:
            c.append(' ' * (len(star[i % m])//2 + 1) + star[i % m] + ' ' * (len(star[i % m])//2+1))
        else:
            c.append(star[i % m] + ' ' + star[i % m])
    star = c
for s in star:
    print(s)