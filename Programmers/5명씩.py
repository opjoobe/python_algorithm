# 프로그래머스 # 5명씩

def solution(names):
    return [names[idx] for idx in range(0, len(names), 5)]

'''
list comprehension & generator
'''
