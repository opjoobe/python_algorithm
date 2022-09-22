# 프로그래머스 # 두 정수 사이의 합

# 풀이 1: 등차수열 공식 S = (n * (a + l)) // 2
def solution(a, b):
    return ((abs(a-b) + 1) * (a + b)) // 2
    
# 풀이 2: 파이썬 range 활용
def solution(a, b):
    return sum(range(a,b+1,1) if a < b else range(b,a+1,1))