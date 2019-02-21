import requests
import re

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108"
filename = open("Data/weather.csv", "w", encoding="ANSI")
received = requests.get(url)
# print(received.text)
text = received.text
temp = re.findall(r'<province>(.+?)</province>', text)
locations = re.findall(r'<location wl_ver="3">.+?</location>', text, re.DOTALL)
temp1 = re.findall(r'<province>(.+?)</province>', locations[0])
print(temp)
print(len(locations))
a, b = (3, 4)
print(a, b)
prov_list = []
city_list = []
data_list = []
mode_list = []
tmEf_list = []
wf_list = []
twn_list = []
tmx_list = []
reli_list = []
# province 와 city를 찾아보세요
for loc in locations:
    prov = re.findall((r'<province>(.+?)</province>'), loc)
    city = re.findall(r'<city>(.+?)</city>', loc)
    pattern = r'<province>(.+?)</province>.+<city>(.+?)</city>'
    prov_city = re.findall(pattern, loc, re.DOTALL)
    # print(prov_city)
    # prov = prov_city[0][0]
    # city = prov_city[0][1]
    # print(prov, city)
    prov_list.append(prov)
    city_list.append(city)
    data = re.findall((r'<data>(.+?)</data>'), loc, re.DOTALL)
    data_list.append(data)

    for datum in data:
        mode = re.findall(r'<mode>(.+?)</mode>', datum)
        tmEf = re.findall(r'<tmEf>(.+?)</tmEf>', datum)
        wf = re.findall(r'<wf>(.+?)</wf>', datum)
        twn = re.findall(r'<tmn>(.+?)</tmn>', datum)
        tmx = re.findall(r'<tmx>(.+?)</tmx>', datum)
        reli = re.findall(r'<reliability>(.+?)</reliability>', datum)
        print(prov[0], city[0], mode[0], tmEf[0], wf[0], twn[0], tmx[0], reli[0], sep=",", file=filename)

filename.close()
# re.findall((r'<province>(.+?)</province>'  ==> <province>에서 </province> 사이의 모든 문자를 가져온다
# re.findall((r'<province>.+?</province>'    ==> <province>에서 </province> 사이의 모든 문자를 가져온다(<province>, </province> 포함해서 가져옴)

