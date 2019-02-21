# import re
# data = ""
# """
# park 800905-1049118
# kim  700905-1059119
# """
#
# data1 = "park 800905-1049118"
# data2 = "kim  700905-1059119"
#
# data1_hi = data1.find("-")
# data2_hi = data2.find("-")
#
# print(data1[data1_hi-6:data1_hi])
# print(data1[data1_hi+1:])
# print(data2[data2_hi-6:data2_hi])
# print(data2[data2_hi+1:])
#
# data = """
# park 800905-1049118
# kim 700905-1059119
# """
# print("***")
# print(data.encode())
#
#
#
# # data_sp = data.split("\n")
# # print(data_sp)
# # data_list = [data_sp[1], data_sp[2]]
# # print(data_list)
# # num = []
# # for i in data_list:
# #     temp = i.split(" ")
# #     num.append(temp[1])
# #
# # str_num = ""
# # num_str = ""
# # hidden_num = []
# # #hidden_num.append(num[0][0:7])
# #
# # for i in num:
# #     hidden_num.append(i[0:8]+"******")
# # print(hidden_num)
# #
# # data1_hip = data_sp[1].find("-")
# # data2_hip = data_sp[2].find("-")
# #
# # # print(data_sp[1][data1_hip-6:data1_hip], end=" ")
# # # print(data_sp[1][data1_hip+1:])
# # # print(data_sp[2][data2_hip-6:data2_hip], end=" ")
# # # print(data_sp[2][data2_hip+1:])
#
#
# pat = re.compile("(\d{6})[-]\d{7}")                     # 앞에 숫자가 6개 그뒤에 "-" 그뒤에 숫자7개인것을 찾는다.
# print(pat.sub("\g<1>-*******", data))
#

# x축은 이름 y축은 백점
import csv
import matplotlib.pyplot as plt
import numpy as np

# x축은 날짜 y축은 최고기온과 최저기온