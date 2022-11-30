# 프로그래머스 # 숫자 찾기

def solution(num, k):
    return str(num).find(str(k)) + 1 if str(k) in str(num) else - 1