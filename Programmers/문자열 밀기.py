# 프로그래머스 # 문자열 밀기

''' Solution 1 : indexing '''
def solution(A, B):
    for i in range(len(A)):
        if A[-i:] + A[:-i] == B:
            return i
    return -1

''' Solution 2 : rotate in deque '''
from collections import deque
def solution(A, B):
    A, B, n = deque(A), deque(B), len(A)
    if A == B: return 0
    for i in range(1, n):
        A.rotate()
        if A == B : return i
    return -1
