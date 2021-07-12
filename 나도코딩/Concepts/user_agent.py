# 개요
# 웹사이트에서는 접속하는 사용자들의 정보를 알 수가 있다. 이를 '헤더 정보'라고 한다.
# ex) 같은 사이트라 하더라도 PC, 모바일 접속 시 보이는 화면이 다름. // 의심되는 사용자에게는 올바를 정보를 주지않음. 이를 user-agent라고 함.
# user agent string 검색 - what is my user agent? 접속 - 파란색 박스 본인 브라우저에서 접속하는 user agent 정보 확인 (심지어 브라우저마다 상이)
# 헤더 정보를 주기 전에는 특정 사이트에서 막을 수도 있지만 user agent를 문자열로 넣어줌으로써 이를 해결하고 정상적인 정보(html)을 받을 수 있음.

import requests
url = "http://nadocoding.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
