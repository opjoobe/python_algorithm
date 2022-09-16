# 프로그래머스 # 올바른 괄호
from collections import deque
def solution(s):
    stack = deque()
    flag = True
    for now in s:
        if now == '(':
            stack.append(1)
        else:
            if not stack:
                flag = False
                break
            stack.pop()
    if stack:
        flag = False
    return True if flag else False