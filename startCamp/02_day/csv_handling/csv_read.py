# 1. split
with open('dinner.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines() # 리스트 형태로 저장
    for line in lines:
        print(line.strip().split(',')) # , 기준으로 문자열을 split한다.

# 2. csv reader
import csv
with open('dinner.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)