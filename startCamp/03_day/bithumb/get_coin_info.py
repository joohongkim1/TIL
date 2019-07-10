import bs4
import requests
import csv

# 1. Bithumb 페이지를 가지고 온다.
response = requests.get("https://www.bithumb.com/")
# print(response) # 응답 객체가 잘 받았는지 확인  # 200 <- status 코드(정상적 응답)
html = response.text # 응답받은 객체에서 html 문서를 string으로  가지고 옴.
# print(html) # <- 타입은? str 

# 2. Beautiful Soup 모듈을 이용하여 string type 의 html 을 파싱한다.
soup = bs4.BeautifulSoup(html, 'html.parser') # string값인 html을 BeautifulSoup를 통해서 파싱 

# 3. 각 코인의 정보가 담겨있는 table row 데이터를 list 의 형태로 가져옴.
coins = soup.select(' .coin_list tr') # 누구 안에 있다 -> 띄어쓰기 하면 됨. 
                                      # coin_list 안에있는 tr을 가져옴 (coin_list안에 tr이 있다면 모두 가져와라)
                                      # > 로 접근하면 상위 바로 다음에 있는 tr만 가져오는 것

# 5. csv writer를 이용해서 정보를 저장한다.
with open('coin_info.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)

# 4. 각 코인을 순회하며 필요한 정보만 추출 

    for coin in coins: # coin == tr
        coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.replace('NEW','').strip()
        coin_price = coin.select_one('td > strong').text.replace(',','').replace('.','')
        data = (coin_name, coin_price)
        print(data)
        csv_writer.writerow(data)
