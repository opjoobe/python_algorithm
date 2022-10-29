# 프로그래머스 # 옹알이 (2)

import re
def solution(babbling):
    return len([1 for word in babbling if re.fullmatch('(aya|ye|woo|ma){1,}', word) and not re.findall('ayaaya|yeye|woowoo|mama', word)])

'''
match 와 findall의 차이를 생각하자.
match는 처음부터 일치하는 것만 찾아주고, findall은 중간에서 일치해도 찾아준다 !
처음에 match로 했다가 일부 케이스 틀림.
'''