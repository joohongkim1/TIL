import requests # 요청을 보낼 수 있는 모듈
import bs4 # Beautiful Soup
url = 'https://finance.naver.com/sise/'

response = requests.get(url) # response.text
print(response)
print(response.status_code)
html = response.text # 응답받은 문서를 text형태로 변환

# print(type(html)) # 타입이 str인지 확인

soup = bs4.BeautifulSoup(html, 'html.parser') # (어떤페이지, 어떤 작업)  parser -> 파싱(접근할 수 있는 형태의 객체로 전환시켜주는 작업)
kospi = soup.select_one('#KOSPI_now').text # soup를 받아와서 text값을 꺼내와라 #
# print(kospi)

