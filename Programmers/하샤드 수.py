# 프로그래머스 # 하샤드 수
def solution(x):
    return True if not x % sum(list(map(int, list(str(x))))) else False