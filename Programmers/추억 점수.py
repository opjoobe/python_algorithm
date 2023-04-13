# 프로그래머스 # 추억 점수

def solution(name, yearning, photo):
    reminiscence = dict(zip(name, yearning))
    return [sum([reminiscence[name] for name in pic if name in reminiscence]) for pic in photo]