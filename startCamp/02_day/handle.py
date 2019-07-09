import os # 윈도우 컴퓨터가 할 수 있는 작업들을 가지고 오는 모듈

os.chdir(r"C:\Users\student\TIL\startCamp\02_day")  # chdir(path) -> 체인지 디렉토리
                                                    # 500개의 지원서가 있는 곳으로 이동 

filenames = os.listdir('.') # listdir() -> 특정 경로에 있는 모든 파일 이름 가져오는 함수   , . -> 현재 디렉토리                                    
for filename in filenames:
    # 확장자가 .txt인 파일만 이름을 바꾼다.
    extension = os.path.splitext(filename)[-1] # 확장자만 따로 분리 # [-1] -> 마지막 인덱스 접근

    if extension == '.txt':
        os.rename(filename, filename.replace('SAMSUNG','SSAFY')) # os.rename('현재파일명', '바꿀 파일명')  f'' <- str 앞에 f쓰면 변수 넣을 수 있음
                                                                 # .replace('현재', '바꿀 것') -> 변경 
