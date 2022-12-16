# 프로그래머스 # 저주의 숫자 3 

def solution(n):
    i, num = 0, 0
    while i < n:
        num += 1
        if num % 3 != 0 and '3' not in str(num): i += 1 # check (num % 3) at first, because it takes less time than ('3' not in str(num)).
    return num