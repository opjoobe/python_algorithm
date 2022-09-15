# 프로그래머스 # 이진 변환 반복하기

def solution(s):
    total = 0
    i = 0
    while s != '1':
        i += 1
        nowLen = len(s)
        nowZero = s.count('0')
        total += nowZero
        s = bin(nowLen - nowZero)[2:]

    answer = [i, total]
    return answer