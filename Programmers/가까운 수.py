# 프로그래머스 # 가까운 수

def solution(array, n):
    return sorted(array, key = lambda x: (abs(x - n), x))[0]

''' 
first option : distance from the given number 'n'
second option : if there's two numbers with the same distance, get smaller one
'''