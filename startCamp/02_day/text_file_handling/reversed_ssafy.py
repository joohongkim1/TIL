# ssafy.txt 파일을 읽어서
# 역순으로 reversed_ssafy.txt 파일로 저장

with open('ssafy.txt', 'r') as f:
    lines = f.readlines() # 각 라인을 item으로 list형태로 반환

lines.reverse() # 리스트에는 해당 리스트를 뒤집는 함수 reverse가 있다.
print(lines)

with open('reversed_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)
     
    
    