id = None
pwd = None
# 아이디 입력
while True:
    id = input('아이디를 입력하세요(3글자 이상) >>>')
    id_conut = 0
    for ch in id:
        id_conut += 1

    if id_conut > 2:
        break

    print('3글자 이상 입력해 주세요!')

# 패스워드 입력
while True:
    pwd = input('>패스워드를 입력하세요 (영문 숫자 포함 8자이상) >>>')
    isContainAlpha = False
    isContainNumeric = False

    if len(pwd) < 8:
        print('패스워드를 입력하세요 (영문 숫자 포함 8자이상) >>>')
        continue

    for ch in pwd:
        if ch.isalpha():
            isContainAlpha = True
        elif ch.isnumeric():
            isContainNumeric = True

    if not isContainAlpha:
        print('>영문 숫자 포함 8자 이상 입력해 주세요!')
        continue

# 영문 포함 유효성 검사
    if not isContainNumeric:
        print('>영문 숫자 포함 8자 이상 입력해 주세요!')
# 숫자 포함 유효성 검사
    pwdChk = input('패스워드 확인 한번 더 입력하세요 >>>')
    if pwd != pwdChk:
        print('> 일치하지 않습니다. 다시 한번 입력해 주세요!')
        continue

    break

print(id)
print(pwd)
print('회원가입 완료!')

# 로그인 아이디
while True:
    loginId = input('아이디를 입력하세요 >>>')
    if id == loginId:
        break
    print('> 아이디가 일치하지 않습니다.')

# 로그인 패스워드
while True:
    loginPwd = input('패스워드를 입력하세요>>>')
    if pwd == loginPwd:
        break
    print('> 패스워드가 일치하지 않습니다')\

print('로그인 성공!')
print('{}님 환영합니다 :)'.format(id))