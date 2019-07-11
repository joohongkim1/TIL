# 딕셔너리 만들기
lunch1 = {
    '중국집': '02'
}
print(lunch1)
lunch2 = dict(중국집='02')
print(lunch2)

# 딕셔너리 내용 추가하기
lunch1['분식집'] = '031'
print(lunch1)

# 딕셔너리 내용 가져오기
idol = {
    'bts': {
        '지민': 24,
        'RM': 25
    }
}

# 랩몬스터의 나이는?
print(idol['bts']['RM'])

print('----------------------------')
# 딕셔너리 반복문 활용하기

# 기본활용
for key in lunch1: # 딕셔너리 for문 돌리면 key값만 나옴
    print(key, lunch1[key])

# value 만 가져오기
for value in lunch1.values(): 
    print(value)

# key 만 가져오기
for key in lunch1.keys(): # .key() 키들의 리스트 반환
    print(key)    

# .items() => key, value 가져오기
for key, value in lunch1.items():
    print(key, value) 
    print(lunch1.items()) 