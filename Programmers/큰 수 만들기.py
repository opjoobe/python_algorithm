# 프로그래머스 # 큰 수 만들기

from collections import deque
def solution(number, k):
    removed = [False] * len(number)
    stack  = deque()
    for idx, num in enumerate(number):
        if k == 0: break
        num = int(num)
        while stack and stack[-1][-1] < num and k > 0:
            removed[stack.pop()[0]] = True
            k -= 1
        stack.append([idx, num])
    while k > 0:
        removed[stack.pop()[0]] = True
        k -= 1
    return ''.join([num for idx, num in enumerate(number) if not removed[idx]])
    
                