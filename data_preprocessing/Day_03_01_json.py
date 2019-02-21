import json
import requests
import re
def not_used_1():
    # d = {"name": "kim", "age":20}
    d = dict(name="kim", age="20")
    print(d)
    d["addr"] = "seoul"
    print(d["name"])
    print((d.keys(), d.values()))
    print(d.items())

    for k, v in d.items():
        print(k, v)


def not_used_2():
    # j1 = {"ip": "8.8.8.8"}              # 딕셔너리 생성
    # print(type(j1))
    # j2 = json.dumps(j1)                 # 딕셔너리를 json 문자열로 변경(str)
    # print(type(j2))
    #
    # j3 = json.loads(j2)                 # json 문자열을 딕셔너리로 변경(dict)
    # print(type(j3))
    # print(j3)

    validation = '''{
       "object_or_array": "object",
       "empty": false,
       "parse_time_nanoseconds": 19608,
       "validate": true,
       "size": 1
    }'''

    j4 = json.loads(validation)
    print(type(j4))
    print(j4.values())
def not_used_3():
    url = "http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt"
    received = requests.get(url)
    text = received.content.decode("utf-8")
    items = json.loads(text)
    print(items)

    code_list, value_list = [], []

    for i in items:
        code_list.append(i["code"])
        value_list.append(i["value"])

    print(code_list)
    print(value_list)

