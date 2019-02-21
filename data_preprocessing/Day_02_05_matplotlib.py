import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib import colors, rc, font_manager



def not_used_1():
    plt.plot([10, 20, 30, 40, 50])
    plt.show()


def not_used_2():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "g--")          # 첫번째리스트 x축 두번째리스트 y축
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
    plt.xlim(0, 5)
    plt.ylim(0, 20)
    plt.show()


# x 의 범위가 -10에서 10일때의 x제곱 그래프를 그려주세요..
# y = x ^ 2
# 리스트로 직접
def not_used_3():
    x_list = []
    y_list = []
    for i in range(-10,11):
        x_list.append(i)
        y_list.append(i**2)

    print(x_list)
    print(y_list)
    plt.plot(x_list, y_list, "ro")
    plt.plot(x_list, y_list, "--")
    plt.show()


def not_used_4():
    # numpy를 이용해서 하는 것
    x_numpy = np.arange(-10, 11)
    print(x_numpy)
    y_numpy = x_numpy**2
    print(y_numpy)

    plt.plot(x_numpy, y_numpy,"ro")
    plt.plot(x_numpy, y_numpy, "--")
    plt.show()


def not_used_5():
    plt.grid(True)
    x1 = np.arange(0.01, 2, 0.01)
    plt.plot(x1, np.sin(x1), "r")
    plt.plot(x1, -np.sin(x1), "g")

    x2 = np.arange(0.01-2, 0, 0.01)
    plt.plot(x2, np.sin(-x2), "b")
    plt.plot(x2, -np.sin(-x2), "k")
    plt.show()


def not_used_6():
    x1 = np.arange(0.01, 2, 0.01)
    plt.subplot(1, 2, 1)                    # 1행 2열로 나눠서 사용한다
    plt.plot(x1, np.log(x1), "r")

    plt.subplot(1, 2, 2)
    plt.plot(x1, -np.log(x1), "g")
    plt.show()


def not_used_7():
    plt.grid(True)
    x1 = np.arange(0.01, 2, 0.01)
    plt.subplot(2, 1, 1)
    plt.plot(x1, np.log(x1), "r")
    plt.subplot(2, 1, 2)
    plt.plot(x1, -np.log(x1), "g")
    plt.figure()
    x2 = np.arange(0.01-2, 0, 0.01)
    plt.subplot(2, 1, 1)
    plt.plot(x2, np.log(-x2), "b")
    plt.subplot(2, 1, 2)
    plt.plot(x2, -np.log(-x2), "k")
    plt.show()

def not_used_8():
    men = [20, 35, 30, 35, 27]
    women = [25, 32, 34, 20, 25]

    n_groups = len(men)
    bar_width = 0.45
    x = np.arange(n_groups)
    # x를 넘파이배열로 만든 이유는 아래의 bar_width 를 계산하기 위해서는 그냥 리스트로는 되지 않기 때문
    # 그래픽 바
    plt.bar(x, men, bar_width, color="b")                   # x = 바의 위치
    plt.bar(x+bar_width, women, bar_width, color="r")
    plt.show()
line_temp = []
#최상위 10개 국가의 GDP 바를 만드시오

font_name = font_manager.FontProperties(fname="C:\Windows\Fonts\malgun.ttf").get_name()
rc("font", family=font_name)

filename = "Data/2016_GDP.txt"

def not_used_9():
    def readCsv_1(filename):
        f = open(filename, "r", encoding="utf-8")
        f.readline()
        #print(f.readline())
        for line in f:
            line_strip = line.strip("\n").replace(",", "")
            line_strip2 = line_strip.split(":")
            line_temp.append(line_strip2)
        f.close()
        return line_temp


    def readCsv_2(filename):
        f = open(filename, "r", encoding="utf-8")
        f.readline()                                # 맨위의 한줄을 읽음
        rows = []
        csv_temp = []
        for row in csv.reader(f, delimiter=":"):
            csv_temp.append(row)
        f.close()
        return csv_temp

    temp = readCsv_1(filename)
    #temp2 = readCsv_2(filename)

    gdp = []
    contry = []
    for i in temp[:30]:
        contry.append(i[0]+"."+i[1])
        gdp.append(int(i[2]))

    plt.title("GDP 순위")
    plt.xlabel("나라")
    plt.ylabel("GDP($)")
    bar_width = 0.45
    plt.bar(contry, gdp, bar_width, color="r")                   # x = 바의 위치
    plt.xticks(rotation=45, size=7)
    plt.tight_layout()
    plt.show()


def not_used_10():
    f = open("Data/2016_GDP.txt", "r", encoding="utf-8")
    f.readline()
    names, dollors = [], []
    for _, name, money in csv.reader(f, delimiter=":"):     # "_" 는 사용하지 않는다는 뜻
        names.append(name)                                  # for문에 여러개의 인자를 사용하기 위해
        dollors.append(int(money.replace(",", "")))
    f.close()

    plt.subplot(1, 2, 1)
    top10_names = names[0:10]
    top10_dollors = dollors[0:10]
    x = np.arange(1,len(top10_names)+1)
    plt.bar(x, top10_dollors, color=colors.TABLEAU_COLORS)
    plt.xticks(x, top10_names, rotation=45, size=7)
    plt.title("TOP 10")
    plt.xlabel("Country")
    plt.ylabel("GDP($)")
    plt.tight_layout()

    plt.subplot(1, 2, 2)

    low10_names = names[(len(names)-10):len(names)]
    low10_dollors = dollors[len(names)-10:len(names)+1]

    x = np.arange(1,len(low10_names)+1)
    plt.bar(x, low10_dollors, color=colors.TABLEAU_COLORS)
    plt.xticks(x, low10_names, rotation=45, size=7)
    plt.title("LOW 10")
    plt.xlabel("Country")
    plt.ylabel("GDP($)")
    plt.tight_layout()

    plt.show()

not_used_10()