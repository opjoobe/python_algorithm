# 프로그래머스 # 괄호 회전하기

from collections import deque
def solution(s):
    parenthesis = {'(':')', '[':']', '{':'}'}
    n = len(s)
    s = deque(s)
    answer = 0
    s.rotate(1)
    for i in range(n):
        s.rotate(-1)
        stack = deque()
        flag = True
        for now in s:
            if now in ('(','[','{'):
                stack.append(now)
            else:
                if stack and parenthesis[stack[-1]] == now:
                    stack.pop()
                else:
                    flag = False
                    break
        if not stack and flag:
            answer += 1
    return answer