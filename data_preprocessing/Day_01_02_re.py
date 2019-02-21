import re
def test_1():
    db = """3412 Bob 123 서울
    3834 Jonny 333 인천
    1248 Kate 634 경기
    1423 Tony 567 충북
    2567 Peter 435 충남
    3567 Alice 535 전북
    1548 Kerry 534 전남
    T4가 Jan Jtn Jnnn Jnre J.n """
    #
    # ns = re.findall(r'[0-9]+', db)       # r : raw
    # print(ns)
    # ns = re.findall(r'[A-Z]+', db)       # r : raw
    # print(ns)
    # ns = re.findall(r"[A-Z][a-z]+", db)
    # print(ns)
    # ns = re.findall(r"[가-힣]+", db)
    # print(ns)
    # ns = re.findall(r"[A-Z][0-9][가-힣]+", db)
    # print(ns)
    # ns = re.findall(r"[^J][a-z]+", db)
    # print(ns)

    # 이름만 찾아보세요
    ns = re.findall(r"[A-Z][a-z]+", db)
    print(ns)
    # T로 시작하는 이름만 찾아보세요
    ns = re.findall(r"T[a-z]+", db)
    print(ns)
    ns = re.findall(r"[A-SU-Z][a-z]+", db)
    print(ns)

    #숫자만 찾아보세요
    ns = re.findall(r"[\d]+", db)
    print(ns)
    ns = re.findall(r'[0-9]+', db)       # r : raw
    print(ns)

    ns = re.findall(r'J.n', db)       # J로 시작해서 n으로 끝나는 문자
    print(ns)

    ns = re.findall(r'J[.]n+', db)       # r : raw
    print(ns)

    ns = re.findall(r'J..n+', db)       # J로 시작해서 둘, 셋 자리를 상관없이 4째자리는 n으로 끝나는것만 출력
    print(ns)
def test_2():
    str_sample = "ct cat caaat cbt"

    ns = re.findall(r"ca*t", str_sample)        # a가 0~무한
    print(ns)
    ns = re.findall(r"ca+t", str_sample)        # a가 1~무한
    print(ns)
    ns = re.findall(r"ca{1,4}t", str_sample)    # a가 1개부터 4개까지
    print(ns)
    ns = re.findall(r"ca?t", str_sample)        # a가 0~1 일경우만 출력
    print(ns)

    p = re.compile("ca?t")
    print("==", p.findall(str_sample))


    str_sample = "abc ac abbc"

    ns = re.findall(r"ab?c", str_sample)        # b가 0~1 일경우만 출력
    print(ns)
    ns = re.findall(r"ab{0,1}c", str_sample)        # b가 0~1 일경우만 출력
    print(ns)

    p = re.compile("[a-z]+")
    m = p.match("python")
    print(m)

def test_3():
    import requests
    # url = "https://www.naver.com"
    url = "http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt"
    received = requests.get(url)
    text = received.content.decode("utf-8")
    print(text)
    #codes = re.findall(r"[0-9]+", text)
    codes = re.findall(r'{"code":"(.+?)",', text)           # code 뒤에 모든 문자를 가져온다는 뜻
    print("codes:",codes)                                   # 괄호를 빼면 code: 도 포함하여 가져옴
    #values = re.findall(r"[가-힣]+", text)
    values = re.findall(r'"value":"(.+?)"', text)
    print(values)
    covel = []
    for i in range(len(values)):
        covel.append((values[i] + " : " + codes[i]))
    print(covel)

test_3()
#test_1()