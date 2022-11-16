# 프로그래머스 # 각도기

def solution(angle):
    return 2 * (angle // 90) if angle % 90 == 0 else 2 * (angle // 90) + 1

    # return 2 * (angle // 90) + (angle % 90 != 0) 으로도 가능 