import requests
import re
import csv


def readCsv_1(filename):
    f = open(filename, "r", encoding="ANSI")
    #print(f.readline())
    for line in f:
        # print(line.strip())                         # 공백으로 나눠서 출력
        # line_replace = line.replace("\n","")
        line_strip = line.strip("\n")
        line_list = line_strip.split(",")
        print(line_list)
    f.close()
    return line_list


def readCsv_2(filename):
    f = open(filename, "r", encoding="ANSI")
    rows = []
    temp = []
    for row in csv.reader(f):                       # csv.reader()함수를 이용하면 리스트로 보내준다
        temp.append(row)
    f.close()
    return temp


def writeCsv_2(filename, data):
    f = open(filename, "w", encoding="ANSI", newline="")
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=":")           # delimiter 는 다음 값을 연결할때 쓰일 문자를 적음
    writer.writerows(data)
    f.close()


if __name__ == "__main__":
    filename = "Data/scores.csv"
    scores_list = readCsv_2(filename)

    # for i in range(len(scores_list)):
    #
    #     if i == 0:
    #         scores_list[0].append("total")
    #         scores_list[0].append("avg")
    #     else:
    #         total = 0
    #         for j in range(2, 6):
    #             total += int(scores_list[i][j])
    #         avg = total/4
    #         scores_list[i].append(total)
    #         scores_list[i].append(avg)
    # print(scores_list)
    #writeCsv_2("Data/scores_result.csv", scores_list)
    print(scores_list)
    writeCsv_2("Data/scores_result.csv", scores_list)
    readCsv_2("Data/sensor.csv")
    # readCsv_2(filename)
