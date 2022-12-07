'''
파일명 : Ex04-6-conditions.py
조건 연산자 (삼항 연산자)
    참 if 조건식 else 거짓
    조건식 결과에 따라 참 또는 거짓으로 결과를 반환 한다.
'''
a = 10
b = 20
result = (a - b) if (a >= b) else (b - a)   # 중요 간단한 분기 처리 할떄 쓰임
print('{}과 {}의 차이는 {}입니다'.format(a, b, result))




