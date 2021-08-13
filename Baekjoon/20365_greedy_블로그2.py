num = int(input())
word = list(input())
word.append("X")

count = 1
for i in range(1, num):
    if word[0] == "B":
        if word[i] == "R":
            count += 1
            if word[i + 1] == "R":
                count -= 1
    else:
        if word[i] == "B":
            count += 1
            if word[i + 1] == "B":
                count -= 1
print(count)
