# 프로그래머스 # 최댓값과 최솟값
def solution(s):
    L = list(map(int, s.split()))
    return '{0} {1}'.format(min(L), max(L))