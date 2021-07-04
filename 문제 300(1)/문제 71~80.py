

# 튜플 : 리스트와 거의 유사 [] -> ( )
    # 단점 : 튜플은 값을 바꿀 수가 없다
    # 튜플명 = ( 값1, 값2, 값3 ~~ 등 )


# 071   튜플 생성 ( 튜플이 뭔지 까먹어서 참고함 )
my_variable = ( )

# 072   튜플 저장하기
my_movie = ("닥터스트레인지", "스플릿", "럭키")

# 073   튜플 생성하기
a = (1)
print(a)

# 074   오류 발생 원인 설명하기
# t = (1,2,3)
# t[0] = 'a'    # 튜플 값은 바꿀 수 없기 때문에 오류가 발생한다

# 075   데이터 타입 찾기
t = 1, 2, 3, 4
print(type(t)) # tuple

# 076  이따 쌤한테 물어보기...

# 077   튜플을 리스트로 변경하기
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(tuple(interest))
        # tuple( ) : 튜플로 변경하기

# 078   리스트를 튜플로 변경하기
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(list(interest))
        # list( ) : 리스트로 변경하기

# 079   실행결과 예상하기
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)      # apple banana cake 출력
                    # 이유는 잘 모르겟음...

# 080   range 함수 ( 참고 )
a = tuple(range(2, 100, 2))
print(a)

# 081   별 표현식 ( 참고 )
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
print(*scores)
*scores,_,_ = scores
print(scores)