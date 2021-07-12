# 이하의 라이브러리들을 제대로 설치했음에도 불구하고 오류가 난다면 해당 py파일이름이 라이브러리명과 동일하기 때문이다. 바꿔주면 손쉽게 해결 가능.

# bs4 - 스크래핑을 위한 패키지
# lxml - 구문 분석 parser

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")
# 본인이 가져온 html문서를 lxml parser를 통해서 bs객체로 만든다. 즉, soup이라는 변수가 모든 정보를 다 가지고 있는 것.

# 첫번째 자식요소 객체(element node) 가져오기
print(soup.a)   # soup내에 있는 첫번째 a element 출력
print(soup.title)

# text node 가져오기
print(soup.title.get_text())    # 첫번째 title element의 text node만 가져옴

# 속성 가져오기
print(soup.a.attrs)   # 딕셔너리 형태로 a element 의 속성들 출력

# 속성 값 가져오기
print(soup.a["href"])   # a element의 속성들 중 원하는 속성의 값 출력

# 위의 방법들은 해당 페이지에 대한 이해가 높을시 사용하면 유용하다.
# 일반적으로 웹스크래핑을 하려는 페이지에 대해 이해도가 낮기 때문에 아래의 방법을 이용하자.


print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# 해당 attrs("class":"Nbtn_upload")를 가지고있는 a element 중 첫번째 element 가져옴.
print(soup.find(attrs={"class": "Nbtn_upload"}))
# element 노드는 생략도 가능. 앞에 써주는 것은 더 정확하게 하기위한 용도일 뿐이고 없다면 해당하는 모든 element가져옴
# attrs도 생랼하고 "element"만 써줘도 가능할 듯하다.

print(soup.find("li", attrs={"class": "rank01"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a)    # rank1중 a element 가져옴


# 이렇게 element들을 가져올 수도 있지만 부모, 자식, 형제요소에도 접근 가능 하다.


print(rank1.a.get_text())

# 다음 형제 요소 가져오기
# print(rank1.next_sibling)
# 이렇게는 정보를 가져올 수 없다. 요소 노드 사이에는 텍스트 노드도 있는데 이 텍스트 노드는 개행 문자인 줄바꿈도 포함한다.
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())   # a를 붙여주는 이유는 rank3만 했을 때는 개행, 공백 문자까지 포함되어서 나온다.

# 이전 형제 요소 가져오기
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

# 형제 요소 가져올 때 두번쓰는 것 줄이기
rank2 = rank1.find_next_sibling("li")   # 인자 부분에는 '가져 올 element'를 입력한다.
print(rank2.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

# 한번에 형제 요소 모두 가져오기
rank2 = rank1.find_next_siblings("li")
# 현재 rank2는 여러 element들이 나오기 때문에 rank2.a 이렇게 찾을수없음. 이건 하나의 element에서만 찾기 가능.
print(rank2)

# 부모 요소 가져오기
print(rank1.parent)
