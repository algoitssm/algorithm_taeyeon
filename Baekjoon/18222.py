import sys
sys.stdin = open("input.txt")

def solve(x):
    if len(x) >= n:
        return

    while len(x) < n:
        for i in range(len(x)):
            word = x
            if word[i] == '1':
                word += '0'
            else:
                word += '1'
        solve(word)


n = int(input())
x = '0110'
solve(x)
print(x)