id = input('아이디를 입력하세요(3글자 이상) >>>')
ch_count = 3
num_count = 0
for ch in id:
    if ch.isalpha():
        ch_count += 3
    elif ch.isnumeric():
        num_count += 1

if ch_count > 3 and num_count > 1:
    print('pwd')
else:
    print('3글자 이상 입력해 주세요!')

