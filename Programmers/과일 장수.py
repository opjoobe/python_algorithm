# 프로그래머스 # 과일 장수

# solution 1 : use 'Counter'
from collections import Counter
def solution(k, m, score):
    revenue, apples = 0, 0
    for p, p_apple in sorted(Counter(score).items(), key = lambda item : item[0] , reverse = True):
        apples += p_apple
        if apples >= m : # if there's more than m apples, make boxes as many as possible.
            boxes, apples = divmod(apples, m)
            revenue += (p * m) * boxes
    return revenue
            
# solution 2 : a little bit slower than #1, but it's simple. get the sum of every p in each boxes , and multiply by m. 
def solution(k, m, score):
    return sum(sorted(score)[len(score) % m : : m]) * m