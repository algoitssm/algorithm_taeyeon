n = int(input())
str_list = [] 
for i in range(1, n + 1):
    str_list.append(str(i))
# print(str_list)

for str_l in str_list:
    cnt = 0
    if '3' in str_l:
        cnt += str_l.count('3')
    if '6' in str_l:
        cnt += str_l.count('6')
    if '9' in str_l:
        cnt += str_l.count('9')
    if cnt == 0:
        print(str_l, end = ' ')          
    else:
        print('-'*cnt, end = ' ') 

# 문자열말고 자릿수 숫자로도 풀어보깅