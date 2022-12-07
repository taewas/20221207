'''
파일명:Ex02-2-variable.py

변수(variable)
어떤 데이터를 저장하고자 할 때 사용하는 메모리 저장소.

변수명 규칙
      영문, 한글, 숫자, 밑줄(_)로 구성된다. (한글로 사용하면 욕 먹을수 있음, 거의 한글 사용안함X)
      특수문자(!@#$%^&*()+ 등) 사용할 수 없다!
      대문자와 소문자를 구분한다.
      변수명의 첫 글자를 숫자로 사용할 수 없다!!
      키워드 ( list, dict, if, for, and 등) 사용할 수 없다!!
'''
'''
name = alice
print(name)
age = 25
prinr(age)
'''
address ='''우편번호 12345
서울시 영등포구 여의도동 1234-5
'''


print(address)



'''
잘못된 변수명 예시
'''
#주석 단축키 # ctrl + / 주석 단축키
# 2mybar = 'python1'
# my-var = 'python2'
# my var = 'python3'

'''
여러 값 할당 
     python을 사용하면 한 줄에 여러 변수에 값을 할당할 수 있다.
'''

x, y, z = "피카츄", "라이츄", "파이리"
print(x)
print(y)
print(z)


'''
여러 변수에 대한 하나의 값
      한줄게 여러 변수에 동일한 값을 할당할 수 있다.
'''

x = y = z = '꼬부기'
print(x)
print(y)
print(z)
