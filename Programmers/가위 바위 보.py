# 프로그래머스 # 가위 바위 보

def solution(rsp):
    return ''.join([dict(zip('205', '052'))[s] for s in rsp])