import csv
import matplotlib.pyplot as plt
from matplotlib import colors, rc, font_manager
import numpy as np
import sys
# x축은 날짜 y축은 최고기온과 최저기온
font_name = font_manager.FontProperties(fname="C:\Windows\Fonts\malgun.ttf").get_name()
rc("font", family=font_name)
plt.rcParams["axes.unicode_minus"] = False
# 마이너스 폰트깨짐 방지

def readCsv_2(filename):
    f = open(filename, "r", encoding="utf-8")
    rows = []
    temp = []
    for row in csv.reader(f):                       # csv.reader()함수를 이용하면 리스트로 보내준다
        temp.append(row)
    f.close()
    return temp

# input_loc = input("지역을 입력하세요 : ")
weather_temp = readCsv_2("Data/weather1.csv")

wt_time = []
wt_low = []
wt_high = []
print(sys.argv)             # 현재 실행되는 파일의 위치

plt.subplot(2, 1, 1)
for i in weather_temp:
    if i[1] == sys.argv[1]:
        wt_time.append(i[3])
        #wt_time.append(i[1]+i[3])
        wt_low.append(float(i[5]))
        wt_high.append(float(i[6]))
plt.plot(wt_time, wt_low,"bo-")
plt.plot(wt_time, wt_high,"ro-")
plt.title("{0} 의 날씨".format(sys.argv[1]))
plt.xticks(rotation=30, size=7)
plt.grid(True)
plt.tight_layout()

wt_time = []
wt_low = []
wt_high = []
plt.subplot(2, 1, 2)
for i in weather_temp:
    if i[1] == sys.argv[2]:
        wt_time.append(i[3])
        #wt_time.append(i[1]+i[3])
        wt_low.append(float(i[5]))
        wt_high.append(float(i[6]))
plt.plot(wt_time, wt_low,"bo-")
plt.plot(wt_time, wt_high,"ro-")
plt.title("{0} 의 날씨".format(sys.argv[2]))
plt.xticks(rotation=30, size=7)
plt.grid(True)
plt.tight_layout()

plt.show()
