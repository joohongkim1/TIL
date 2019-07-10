from flask import Flask # 모듈을 임포트 시켜서 파이썬 파일을 실행할 수 있다. ex) import hello
import datetime
import random
app = Flask(__name__)

@app.route("/") # 데코레이터 , endpoint
def hello(): # def : 함수 생성 , -> Hello Ssafy를 반환하는 hello라는 함수를 만듦.
    return "Hello Ssafy!"

@app.route('/ssafy')
def ssafy():
    return 'Hello SSAFY'

@app.route('/dday') # /가 항상 앞에 붙어야 한다. 안 그러면 인식 못함.
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 5, 21)
    td = b_day - today
    return f'{td.days} 일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag! </h1>'

@app.route('/html_lines')
def html_lines():
    return '''
    <h1>여러 줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''

# Variable Routing
@app.route('/greeting/<name>') # IU
def greeting(name): # name == IU
    return f'반갑습니다! {name}님'

@app.route('/cube/<int:num>')  # int값을 넣되, 이름을 num으로 지정
def cube(num):
    return f'{num}의 3제곱은 {num ** 3} 입니다.'

# 실습
@app.route('/lunch/<int:people>')
def lunch(people):
    # 사람 수 만큼의 랜덤 아이템을 menu list에서 
    # 뽑아서 보여주는 페이지 작성
    menu = ['부대찌개', '김치찌개', '된장찌개']
        # random.sample # 특정 사람수만큼 뽑는 함수
    order = random.sample(menu, people)
    return str(order)

 



if __name__ == '__main__':
    app.run(debug=True)