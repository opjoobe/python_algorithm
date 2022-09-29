# 프로그래머스 # 부족한 금액 계산하기

# 첫번째 풀이
def solution(price, money, count):
    now = price * sum(range(1, count + 1)) - money
    return now if now > 0 else 0

# 두번째 풀이 (한줄풀이)

def solution(price, money, count):
    return max(price * (1 + count) * count // 2 - money, 0)

# 세번째 풀이 (한줄풀이 v2)

def solution(price, money, count):
    return max(price * (1 + count) * count // 2 - money, 0)

''' 등차수열을 통해 계산하면 수행속도가 압도적으로 빠르다. '''