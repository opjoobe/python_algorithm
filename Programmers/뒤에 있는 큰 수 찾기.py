# 프로그래머스 # 뒤에 있는 큰 수 찾기

from collections import deque
def solution(numbers):
    stack = deque()
    answer = [-1] * len(numbers)
    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(idx)
    return answer