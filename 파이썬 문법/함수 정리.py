# 1. print()_함수
#     정의 : 출력할떄 쓰이는 함수
#     사용 방법 : print()의 ()안에 출력을 할 것을 ""와 함꼐 적음
#
# 2. type() int() str() float() 함수
#     정의 : 출력하는 값이 무슨 형태인지 알 수 있음
#     사용 방법 : print()와 같이 쓰일 수도 있고 () 안에 정수를 입력하여 쓰일 수 있음
#
# 3. 인덱싱
#     정의 : 리스트 등의 어떤것에 번호 등을 통해 순서를 나타내는 것
#
# 4. 슬라이싱
#     정의 : 리스트에 있는 것을 일부만 가져오는 것
#     사용 방법 : [ : ] 형태로 사용할 수 있음
#
# 5. replace() 함수
#     정의 : 저장한 텍스트나 인덱스부터 문자열을 다른 문자열로 바꿔줌
#     사용 방법 : 문자나 특정 문자를 바꿔야 할 때 사용함
#
# 6. split() 함수
#     정의 : 문자열을 일정한 규칙으로 잘라서 리스트로 만드는 것
#     사용 방법 : 문자열.split() 형태로 사용함
#
# 7. % formatting 이란
#     정의 : 문자열 중간에 특정 변수 값을 넣어주기 위해서 사용함
#
# 8. format() 함수
#     정의 : 문자열 중간에 특정 변수 값을 넣어주기 위해서 사용함
#     사용 방법 : "{}".format() 형태로 사용함
#
# 9. f-string
#     정의 : 문자열 중간에 특정 변수 값을 넣어주기 위해서 사용
#     사용 방법 : f"i{i}, j,{j}" 형태로 사용함
#
# 10. strip() rstrip()1strip() 함수
#     정의 : 앞뒤, 오른쪽, 왼쪽 공백 제거 함
#     사용방법 : 앞에 a. 를 붙이는 형태로 사용됨
#
# 11. upper() lower() capitalize() 함수
#     정의 : 대문자, 소문자, 앞글자를 대문자로 만들어줌
#     사용 방법 : 앞에 a. 를 붙이고 사용
#
# 12. endswith() startswith() 함수
#     정의 : 끝나는 문자와 시작하는 문자가 맞는지 확인해줌
#     사용 방법 : 앞에 a. 를 붙여 사용할 수 있음
#
# 13. 리스트와 변수 차이
#     리스트 : 변수를 여러개 저장
#     변수 : 저장 공간
#
# 14. append() insert() del 함수
#     정의 : 리스트에 변수를 추가하고 인덱스 번호에 변수를 추가해주고 원하는 인덱스를 삭제해줌
#     사용 방법 : 리스트명 뒤에 .append() 또는 .insert() 그리고 del 리스트명 형태로 사용함
#
# 15. max() min() sum() len() 함수
#     정의 : 최대값, 최솟값, 합계, 계수를 나타냄
#     사용 방법 : 각 함수 뒤에 (리스트명) 을 통해 사용할 수 있음
#
# 16. join 함수
#     정의 : 리스트에 있는 요소를 합칠 때 쓰임
#     사용방법 : " ".join() 형태로 사용됨
#
# 17. \n \t 제어문자
#     정의 : \n 들여쓰기(enter)
#           \t 띄어쓰기(back space)
#
# 18. 리스트를 오름차순 / 내림차순 방법
#     오름차순 : 리스트명.sort()
#               print(리스트명)
#     내림차순 : 리스트명.sort(reverse=True)
#               print(리스트명)