# 프로그래머스 # 점의 위치 구하기

''' # 1 : with if & else '''
def solution(dot):
    x, y = dot
    if x > 0: return 1 if y > 0 else 4
    return 2 if y > 0 else 3

''' # 2 : simple solution by 1 line, use indexing '''
def solution(dot):
    return [1,4,2,3][2 * (dot[0] < 0) + (dot[1] < 0)]