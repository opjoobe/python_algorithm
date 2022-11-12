# 프로그래머스 # 최댓값 만들기(2)
def solution(numbers):
    numbers.sort()
    n1 = numbers[-1] * numbers[-2]
    n2 = numbers[0] * numbers[1]
    return n1 if n1 > n2 else n2

'''
use max instead... ex) return max(n1, n2)
'''