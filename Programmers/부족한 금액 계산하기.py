# 프로그래머스 # 부족한 금액 계산하기

def solution(price, money, count):
    now = price * sum(range(1, count + 1)) - money
    return now if now > 0 else 0