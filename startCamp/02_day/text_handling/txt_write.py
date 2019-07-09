# 열기모드
# r : 읽기, w : 쓰기(write - 오버라이트(덮어쓰기)), a : 추가(append)
f = open('ssafy.txt', 'w') # 파일 열기
for i in range(10):
    f.write(f'this is line {i + 1}\n') # 작성을 하겠다
f.close() # 파일 작성 다하고 반드시 들어가야됨

with open('with_ssafy.txt', 'w') as f: # 컨텍스트 매니저
    for i in range(10):
        f.write(f'this is line {i+ 1}\n') # with는 해당 구문에서 벗어나면 자동 close , 직접 안해줘도 됨

with open('ssafy.txt', 'w', encoding = 'utf-8') as f: # 한글로 하려면 encoding~
    f.writelines(['0\n', '1\n', '2\n', '3\n']) # 한 번에 여러 텍스트 입력 

    