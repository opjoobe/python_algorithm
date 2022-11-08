# 프로그래머스 # 특이한 정렬

def solution(numlist, n):
    return sorted(numlist, key = lambda x: [abs(n - x), -x])

'''
- 붙이면 내림차순으로 정렬. 여기서의 정렬이 heap을 기반으로 이루어지는 것일까? 아니면 내림차순이라 점차 감소(-)하는 형태라 그런 것일까?
lambda 사용 이유: 메모리 상의 이점.
'''