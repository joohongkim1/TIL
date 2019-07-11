"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
print("==== Q-1 ====")
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
# sum = 0
# for sub_score in score.values():
#     sum+=sub_score
# avg_score = sum / len(score.values())
# print(avg_score)

total = sum(score.values())
avg = total / len(score)
print(avg)


# 2. 반 평균을 구하시오. -> 전체 평균
print("==== Q-2 ====")
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.

# avg1 = (scores['a']['수학']+scores['a']['국어']+scores['a']['음악'])/3
# avg2 = (scores['b']['수학']+scores['b']['국어']+scores['b']['음악'])/3
# sum_avg = (avg1+avg2)/2
# print(avg1,avg2,sum_avg)
total = 0
cnt = 0

for person_score in scores.values():
    total += sum(person_score.values())
    cnt += len(person_score)

avg = total / cnt
print(avg)

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
# for key, value in city.items():
    # print(key + ' :', (value[0]+value[1]+value[2])/3))

"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
total = 0
for key, value in city.items():
    avg_temp = sum(value) / len(value)
    print(f'{key} : {avg_temp:.1f}') 


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
count = 0
for name, temp in city.items():
    # 첫 번째 시행 때
    # 단 한번만 실행되는 조건이 필요해서 count 변수 사용
    if count == 0:
        hot_temp = max(temp)
        cold_temp = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가 cold_temp 보다 낮으면, cold_temp 에 값을 새로 넣고,
        if min(temp) < cold_temp:
            cold_temp = min(temp)
            cold_city = name
        # 최고 온도가 hot_temp 보다 높으면, hot_temp 에 값을 새로 넣는다.
        if max(temp) > hot_temp:
            hot_temp = max(temp)
            hot_city = name
    count += 1

print(f'최고로 더웠던 지역은 {hot_city} {hot_temp} 였고, 최고로 추웠던 지역은 {cold_city} {cold_temp} 였다.')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
if 2 in city['서울']:
    print('네 있어요')
else:
    print('아니요 없어요')