# 04_day

- code . (현재 폴더에서 vs코드 실행)

- flask 는 app.py 이름으로 만들면 좋다.
- flask 앱 -> 서버
- git bash에서 항상 자신이 위치해있는 폴더 확인 



## flask

*** 중요**

- 로그인 창 보여주는 페이지 요청
- 로그인 페이지에서 로그인을 해달라는 요청
- action => form 을 보내는 url 정의하는 곳

- 사용자가 보낸 요청을 확인(Handling)할 수 있는 객체 : request (requests랑 다름, requests는 요청 보내는 것)

- 

1. ascii art라는 end point
2. font 지정 , flask가 ascii art라는 api에게 폰트리스트를 요청 
3. 리스트 중에 하나만 랜덤 초이스
4. 사용자가 보내준 것과 조합을 해서 api에게 make 요청
5. 다시 flask에 전달, flask에서 사용자에게 보여줌



- pre 태그 : 입력받은 문자 그대로를 보여주는 태그