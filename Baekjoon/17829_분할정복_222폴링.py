import sys
sys.stdin = open("input.txt")

def solve(puzzle, n):
    if n == 1:
        print(*puzzle[0])
        return

    new_puzzle = [[0] * (n // 2) for _ in range(n // 2)]
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            temp = []
            temp.append(puzzle[i][j])
            temp.append(puzzle[i+1][j])
            temp.append(puzzle[i][j+1])
            temp.append(puzzle[i+1][j+1])
            temp.sort()
            new_puzzle[i//2][j//2] += temp[-2]
    solve(new_puzzle, n//2)

n = int(input())
puzzle = [list(map(int, input().split())) for _ in range(n)]

solve(puzzle, n)