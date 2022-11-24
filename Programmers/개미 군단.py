# 프로그래머스 # 개미 군단

def solution(hp):
    big, hp = divmod(hp, 5)
    medium, small = divmod(hp, 3)
    return big + medium + small