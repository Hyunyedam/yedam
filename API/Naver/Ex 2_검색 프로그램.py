
# 네이버 검색 ARI 이용한 JSON 가공 프로그램
    # JSON : 키 - 값 => 한쌍 <--딕셔너리와 유사
# 네이버검색 함수 만들기

import os
import sys
import urllib.request
import json
import re

def 네이버검색(카테고리, 검색결과수):

    client_id = "jt0sU0KM6HIUfCtGzPxs"
    client_secret = "D0kGf4ecsj"
    # 검색결과를 json 으로 가져오기
    url = "https://openapi.naver.com/v1/search/"+카테고리 + ".json"
    option = "&display="+검색결과수+"&sort=count"
    query = "?query="+urllib.parse.quote( input(카테고리 + "의 검색 정보 입력 : "))
    url_query = url + query + option

    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    검색결과 = response_body.decode('utf-8')  # utf-8 : 한글지원
    # 검색결과 가공 하기
    json결과 = json.loads(검색결과)
    for i in json결과['items']:
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print("-----> 검색결과 : " + 타이틀)

        if 카테고리 == "shop":
            print('----> 최저가 :', i['lprice'])
        if 카테고리 == "movie":
            print('----> 평점', i['userRating'])
        if 카테고리 == 'news':
            print("----> 주요내용 : ", i['description'])

# 프로그램 코드
while True : # 무한반복하기
    print("검색[NaverARI] 프로그램")
    print("카테고리 [1.뉴스 2.쇼핑 3.도서 4.영화 5.백과사전] 0.종료")
    선택 = int(input("선택 : ")) # 입력받아 선택변수에 저장
    # 선택 제어
    if 선택 == 1 :
        카테고리 = "news"
        검색결과수 = input("--> 뉴스를 선택 했습니다. 몇개 출력할까요?")
        네이버검색( 카테고리 , 검색결과수 )
    if 선택 == 2 :
        카테고리 = "shop"
        검색결과수 = input("--> 쇼핑을 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 3 :
        카테고리 = "book"
        검색결과수 = input("--> 책을 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 4 :
        카테고리 = "movie"
        검색결과수 = input("--> 영화를 선택 했습니다. 몇개 출력할까요?")
    if 선택 == 5:
        카테고리 = "encyc"
        검색결과수 = input("--> 백과사전을 선택 했습니다. 몇개 출력할까요?")
        네이버검색(카테고리, 검색결과수)
        네이버검색(카테고리, 검색결과수)
    if 선택 == 0 :
        print("--> 이용해주셔서 감사합니다.")
        break # 반복문 종료 : while문 탈출