from flask import Flask, render_template, request # 사용자의 요청을 확인할 수 있음.
import requests
app = Flask(__name__)

@app.route('/')  # 사용자가 들어올 수 있는 경로를 정의해준다.(어떤 페이지를 보여줄지)
                 # / => root , ex) www.google.com/search           
def index(): # 어떤 정보로 응답을 해줄지 정의
    return 'Hello World'

@app.route('/greeting1/<string:name>')
def greeting1(name):
    return f'Hello {name}'

@app.route('/greeting/<name>') # <> 안 값이 디폴트값 스트링 , <string:name>으로 적어주는 것도 좋다
def greeting(name):
    return render_template('greeting.html', html_name=name)

@app.route('/ping')
def ping():
        return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get ('age') # 사용자가 보낸 args를 get해서 처리
    return f'Pong! age: {age}'


@app.route('/google')    
def google():
    return render_template('google.html')

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ascii_input')
def ascii_input(): # 사용자가 입력하는 페이지 하나 생성
    return render_template('ascii_input.html')

@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text') # input의 name을 text로 정했기 때문
    # Ascii art API 를 활용해서 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html', result=result) 

    
if __name__ == '__main__':
    app.run(debug=True)