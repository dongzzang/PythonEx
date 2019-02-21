import re
import csv

filename = "Data/2017_GDP.txt"
f = open(filename, "r", encoding="utf-8")
temp = f.readlines()

index_list, name_list, money_list = [], [], []
for i in temp:
    index = re.findall(r"\|\| ([0-9]+)\|\|", i)
    name = re.findall(r"\[\[(.+?)\]\]", i)
    money = re.findall(r"\]\]\|\| (.+?)\|\|", i)

    index_list.append("".join(index))
    name_list.append("".join(name))
    money_list.append("".join(money))


print(index_list)
print(name_list)
print(money_list)
for i in range(len(money_list)):
    #print(money_list[i])
    money_split = money_list[i].split("만")
    if len(money_split[1]) == 0:
            money_split[1].insert(0,"0000")
    if len(money_split[1]) == 1:
        money_split[1].insert(0, "000")
    if len(money_split[1]) == 2:
        money_split[1].insert(0, "00")
    if len(money_split[1]) == 3:
        money_split[1].insert(0, "0")
    print(money_split[1])

