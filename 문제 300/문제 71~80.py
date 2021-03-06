
# 튜플 : 리스트와 거의 유사 [] -> ( )
    # 단점 : 튜플은 값을 바꿀 수가 없다
    # 튜플명 = ( 값1, 값2, 값3 ~~ 등 )

# 문제 71     # 튜플 만들기
my_variable = ( ) # 튜플 생성

# 문제 72     # 튜플 저장하기
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 문제 73     # 숫자 1이 저장된 튜플 생성하기
my_tuple = (1)
print(type(my_tuple)) # int 정수  # 튜플이 아니다
my_tuple = (1, ) # ( , ) 추가
print(type(my_tuple)) # tuple  # 튜플로 생성

# 문제 74     # 오류가 발생하는 원인 찾기
# t = (1, 2, 3)
# t[0] = 'a'  # 0번째 순서의 값을 a로 변환
    # 오류 발생 이유 : 튜플은 값을 바꿀수가 없음

# 문제 75     # t에는 1, 2, 3, 4 데이터가 바인딩 되어있을때, t가 바인딩하는 데이터의 타입 찾기
t = 1, 2, 3, 4
print(type(t))  # t의 타입은 튜플

# 문제 76     # 변수 t에는 아래와 같은 값이 저장되어 있을 때, t가 ('A', 'b', 'c') 튜플을 가리키도록 수정하기
t = ('a', 'b', 'c')
t[0] = 'A'
    # 오류 발생 이유 : 튜플은 값을 바꿀 수 없다.

# 문제 77     # 튜플을 리스트로 변환하기
interest = ("삼성전자", "LG전자", "SK Hynix")
print(list(interest))
    # List(튜플) : 리스트로 변환

# 문제 78
interest = ["삼성전자", "LG전자", "SK Hynix"]
print(tuple(interest))
    # tuple(리스트 명) : 튜플로 변환

# 문제 79     # 코드의 실행 결과 예상하기
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
    # 팩킹[ 묶음 ] : 리스트, 튜플, 딕서너리
    # 언팩킹[ 묶음 x ] : 데이터 한개 [ 변수 ]

# 문제 80     # 1~99 중 짝수만 저장된 튜플을 출력하기
data = tuple(range(2, 100, 2))
print(data)
    # range(시작값, 끝값, 증가단위)