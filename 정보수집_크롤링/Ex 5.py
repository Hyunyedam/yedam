
# 현재 은 가격 크롤링

from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib

주소 = 'https://finance.naver.com/marketindex/worldGoldDetail.nhn?marketindexCd=CMDT_SI&fdtc=2'
웹문서 = ur.urlopen(주소)
soup = bs(웹문서.read(), 'html.parser')
가격 = soup.find_all('p', {"class":"no_today no_today_world"})
은가격 = 가격[0].text.split("1")
print(은가격[0])