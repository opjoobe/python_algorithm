# 프로그래머스 # OX퀴즈

def solution(quiz):
    return ["O" if eval(q.replace("=","==")) else "X" for q in quiz]