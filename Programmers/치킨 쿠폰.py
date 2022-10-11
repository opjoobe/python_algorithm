# 프로그래머스 # 치킨 쿠폰

def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, rest = divmod(chicken, 10)
        answer += chicken
        chicken += rest
    return answer