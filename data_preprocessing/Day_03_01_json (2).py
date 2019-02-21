import json
import requests

def not_used_1():
    # dictionary
    # 영한 사전 : 영어 단어를 찾으면 한글 설명
    # 영어 단어 : key
    # 한글 설명 : value

    #      key   value
    # d = {'name': 'kim', 'age': 20}
    d = dict(name='kim', age=20)
    print(d)

    d['addr'] = 'seoul'
    print(d['name'])

    print(d.keys())
    print(d.values())
    print(d.items())

    for k, v in d.items():
        print(k, v)

    for k in d:
        print(k, d[k])

j1 = {'ip':'8.8.8.8'}   # 딕셔너리 생성
print(type(j1))

j2 = json.dumps(j1)     # 딕셔너리를 json 형식으로 변경
print(type(j2))         # str형
print(j2)

j3 = json.loads(j2)
print(type(j3))
print(j3)

# ------------------ #

# 문제
# json 문자열에서 value만 출력해주세요.
validation = '''{
   "object_or_array": "object",
   "empty": false,
   "parse_time_nanoseconds": 19608,
   "validate": true,
   "size": 1
}'''



