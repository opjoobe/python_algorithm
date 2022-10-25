# 프로그래머스 # 삼각형의 완성조건(2)

def solution(sides):
    return len(range(max(sides) - min(sides) + 1, sum(sides)))