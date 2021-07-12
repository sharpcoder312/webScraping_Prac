# 정규식 라이브러리를 가져다 씀
import re

p = re.compile("ca.e")  # 패턴 = 정규식 컴파일
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (0) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (o) | face (x)

def print_match(m):
  if m:
    print(m.group())    # group() - 매칭되면 출력 | 매칭되지않으면 error
  else:
    print("매칭할 값 없음")

m = p.match("case")   # match() - 인자로 비교하려는 값을 넣어준다. 주어진 문자열의 처음부터 일치하는지 확인 ∴ good care(매칭X)
print_match(m) 
