import requests

url = "https://comic.naver.com/webtoon/weekdayList?week=thu"
res = requests.get(url)
res.raise_for_status()  # 웹스크래핑을 위한 html파일을 잘 가져왔는지 검사

# 위 raise_for_status()메서드를 아래와 같이 if문으로 표현할 수도 있다.
# print(response)  get이 정상적으로 잘 작동하는지 검사  // 200 - 정상 // 403 - html파일 정상적으로 불러올수없음 ∴ 다른 방법 써야함
# print("응답코드 :", res.status_code)
# if res.status_code == requests.codes.ok:
#     print("정상 작동")
# else:
#     print("문제가 있습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))    # 가져오는 html파일의 text 개수 검사
print(res.text)

# 가져온 text를 html파일로 만들어서 보기. // w - 쓰기모드 // f는 그냥 이름임
with open("mywebtoon.html", "w", encoding="utf8") as f:
    f.write(res.text)
