# 프로그래머스 # 푸드 파이트 대회

def solution(food):
    left_food = ''
    for i, cnt in enumerate(food[1:],1):
        left_food += str(i) * (cnt // 2)
    return left_food + '0' + left_food[::-1]