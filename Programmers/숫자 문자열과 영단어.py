# 프로그래머스 # 숫자 문자열과 영단어

# import re
def solution(s):
    numDict = dict(zip(['zero','one','two','three','four','five','six','seven','eight','nine'],list(map(str, range(10)))))
    # re.findall('[a-z]+', s) 이걸 이용해서 정규표현식으로 한줄로 할순 없을까
    for numString in numDict:
        s = s.replace(numString, numDict[numString])
    return int(s)