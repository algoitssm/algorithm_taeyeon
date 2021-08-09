words = input()
words = words.replace('XXXX','AAAA')
words = words.replace('XX','BB')

if 'X' in words:
    final = -1
else:
    final = words

print(final)
