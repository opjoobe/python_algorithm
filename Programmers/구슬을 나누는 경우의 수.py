# 프로그래머스 # 구술을 나누는 경우의 수
from math import factorial
def solution(balls, share):
    return factorial(balls) / (factorial(balls - share) * factorial(share))