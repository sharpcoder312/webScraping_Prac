# 정규식 라이브러리를 가져다 씀
import re

p = re.compile("ca.e")  # 패턴 = 정규식 컴파일


def print_match(m):
    if m:
        print("m.proup():", m.group())    # group() - 일치하는 문자열 반환
        print("m.string():", m.string)    # string() - 입력받은 문자열 반환
        print("m.start():", m.start())    # start() - 일치하는 문자열의 시작 index 반환
        print("m.end():", m.end())    # end() - 일치하는 문자열의 끝 index 반환
        print("m.span():", m.span())    # span() - 일치하는 문자열의 시작 | 끝 index 반환
    else:
        print("매칭되지않음")


m = p.match("case")   # match - 주어진 문자열의 처음부터 일치하는지 확인 ∴ good care(매칭X)
print_match(m)

m = p.search("good care")   # search : 주어진 문자열 중에 일치하는게 있는지 확인 ∴ good care(매칭o)
print_match(m)

lst = p.findall("good care cafe")  # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)


# 정규식 정리
# 1. p = re.compile("원하는 형태") - 보통 p로 받음
# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (0) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (o) | face (x)

# 2. m = p.match("비교할 문자열") - 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") - 주어진 문자열 중에 일치하는게 있는지 확인
# 3. lst = p.findall("비교할 문자열") - 일치하는 모든 것을 "리스트" 형태로 반환
