words = input()                               # 데이터를 받아온다.
words = words.replace('XXXX','AAAA')          # 선 : repalce를 이용해 XXXX->AAAA로 변경
words = words.replace('XX','BB')              # 후 : replace를 이용해 XX->BB로 변경

if 'X' in words:                              # X가 아직 존재하는 경우 final -1로 출력
    final = -1
else:
    final = words                             # 이외의 경우 words를 final로 지정하여 출력

print(final)
