import requests
url = "https://www.naver.com"

received = requests.get(url)
print(received)
print(received.text)
