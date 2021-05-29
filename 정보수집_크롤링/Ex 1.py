
from bs4 import BeautifulSoup as bs
import urllib.request as ur

# 1. 인터넷 주소 넣기
url = 'http://quotes.toscrape.com/'

# 2. 해당(url) 인터넷을 파이썬에서 열기해서 html 변수에 저장
html = ur.urlopen( url )

# 3. read() : 인터넷을 읽어오기
soup = bs(html.read() , 'html.parser')

# 4. 읽어온파일중 찾기 ('span') 찾아서 첫번째 텍스트 가져오기
print(soup.find_all('span')[0].text)
#    마크업 언어 [html] 에서 <span> 태그를 찾아서 태그 사이에 있는 텍스트 가져오기

# find_all( ) : 찾는 값 모두 가졍괴
print(soup.find_all('span')[4].text)

# 모든 span 출력
for i in soup.find_all('span'):
    print(i.text)

# div 태그 포함된 해당 클래스만 찾기
for i in soup.find_all('div', {"class":"quote"}):
    print(i.text)