import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 전체 element 가져오기
# cartoons = soup.find_all("a", attrs={"class": "title"})
# for cartoon in cartoons:    # Js의 for of문이랑 비슷한 것 같다.
#     print(cartoon.get_text())
# 해당 attrs("class": "title")를 가지고있는 a element를 모두 가져옴


# n번째 element 가져오기
# cartoons = soup.find_all("td", attrs={"class": "title"})
# print(cartoons[0].a.get_text())
# title[]에서 바로 텍스트 가져오면 개행문자인 줄바꿈까지 포함하여 출력됨.


# n번째 element의 속성 값 가져오기
# link = cartoons[0].a["href"]
# print("https://comic.naver.com" + link)


# 전체 element의 속성 값 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)


# 평점 가져와서 평균내기
total_rates = 0
cartoons2 = soup.find_all("div", attrs={"class": "rating_type"})
for cartoon in cartoons2:
    rate = cartoon.strong.get_text()  # strong을 .find("strong")으로 입력해도 동일하다.
    print(rate)
    total_rates += float(rate)
average_rate = total_rates / len(cartoons2)
print(total_rates)
print(average_rate)

# tip01 ) 터미널창에 python을 입력하고 실행하여 idle처럼 위 코드들의 실행 결과를 바로바로 보면서 작업할 수도 있다. - 시간을 줄이는데 용이함.
# exit()로 빠져나올 수 있음.

# tip02 ) beautifulSoup는 한글 문서가 제공되기 때문에 포털에 들어가서 더 많은 예제와 설명들을 볼 수 있다.
