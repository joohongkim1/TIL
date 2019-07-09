dinner = {
    '양자강': '02-557-4211',
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887',
}

# print(dinner.keys()) # .keys -> key값만 가져올 수 있음, 리스트 타입으로 반환
# print(dinner.values()) 
# print(dinner.items()) -> key값과 value 두개 다 가져옴.

# 1. String formatting 
with open('dinner.csv', 'w', encoding='utf-8') as f:
    for item in dinner.items():  # 딕셔너리를 item형식으로 변경
        f.write(f'{item[0]},{item[1]}\n') # ex) 양자강,02-557-4221

# 2. CSV writer 
import csv
with open('dinner.csv', 'w', encoding='utf-8', newline='') as f: 
    # 매개변수에서 옵션으로 줄 경우에는 '=' 앞 뒤에 공백없이 작성
    csv_writer = csv.writer(f) # f라는 파일에 csv를 작성하는 객체를 생성
    for item in dinner.items():
        csv_writer.writerow(item)
        #파일 마지막에는 빈 한 줄을 만들어줄 것
