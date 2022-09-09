# 프로그래머스 # 나머지가 1이 되는 수 찾기
def solution(n):
    answer = 0
    x = 2
    while True:
        if n % x == 1:
            return x
        x += 1