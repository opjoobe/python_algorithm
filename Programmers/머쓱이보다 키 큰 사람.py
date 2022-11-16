# 프로그래머스 # 머쓱이보다 키 큰 사람

# Solution 1 : use Binary Search (bisect)
from bisect import bisect_right
def solution(array, height):
    return len(array) - bisect_right(sorted(array), height)

# Solution 2 : use 'index' method of List
def solution(array, height):
    return sorted(array + [height], reverse = True).index(height)