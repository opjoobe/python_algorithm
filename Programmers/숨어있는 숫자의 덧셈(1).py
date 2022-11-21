# 프로그래머스 # 숨어있는 숫자의 덧셈(1)

def solution(my_string):
    return sum([int(x) for x in my_string if x.isdigit()])