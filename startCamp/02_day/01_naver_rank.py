import bs4
import requests

url = 'https://www.naver.com/'

# 아이디는 #으로 접근, 클래스는 .으로 접근 

# '.ah_1 .ah_item .ah_a .ah_k'  # 띄어쓰기는 그 안에서 다시 검색

selector = '.ah_l .ah_item .ah_a .ah_k'

html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')
ranks = soup.select(selector)

for rank in ranks:
    print(rank.text)