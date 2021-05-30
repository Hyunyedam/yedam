
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
    url = "https://openapi.naver.com/v1/search/" + 카테고리 + ".json"
    option = "&display=" + 검색결과수 + "&sort=count"
    query = "?query=" + urllib.parse.quote(input(카테고리 + "의 검색 정보 입력 : "))
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

        if 카테고리 == "movie":
            print('----> 평점', i['userRating'])
            print('----> 감독', i['director'])
            print('----> 영화배우', i['actor'])

# 프로그램 코드
while True : # 무한반복하기
    print("검색[NaverARI] 프로그램")
    print("카테고리 [4.영화] 0.종료")
    선택 = int(input("선택 : ")) # 입력받아 선택변수에 저장
    # 선택 제어

    if 선택 == 4 :
        카테고리 = "movie"
        검색결과수 = input("--> 영화를 선택 했습니다.")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 0 :
        print("--> 이용해주셔서 감사합니다.")
        break # 반복문 종료 : while문 탈출