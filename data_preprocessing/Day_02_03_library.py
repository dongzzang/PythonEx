import re
import requests
url = "http://211.251.214.169:8080/SeatMate3/SeatMate.php?classInfo=3"

received = requests.get(url)
text = received.content.decode("ANSI")
#print(text)
ava_list = []
seat = re.findall(r'<div d=0(.+?)<div', text)
for lo in seat:
    ava = re.findall(r"좌석번호:(.+)'>", lo)
    ava_list.append(ava)
print(ava_list)
print(ava_list[0])
#ava = re.findall(r'좌석번호:(.+?)', seat)
print("he",seat[0])
#print(ava)

empty = re.findall(r'>([0-9]+)</div></div>', text)
print(empty)

empty = re.findall(r"'좌석번호:([0-9]+)'><div", text)
print(empty)

