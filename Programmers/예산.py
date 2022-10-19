# 프로그래머스 # 예산

# 풀이 1: combinations 활용
from itertools import combinations 
def solution(d, budget): 
    d = sorted(d) 
    for department_cnt in range(len(d), 0, -1): 
        if sum(d[:department_cnt]) > budget: 
            continue 
        for case in combinations(d, department_cnt): 
            if sum(case) <= budget: 
                return department_cnt 
    return 0

# 풀이 2: 이분탐색
from itertools import combinations
def solution(d, budget):
    d = sorted(d)
    start, end = 0, len(d)
    while start <= end:
        mid = (start + end) // 2
        if sum(d[:mid]) <= budget:
            start = mid + 1
        else:
            end = mid - 1
    return end

# 풀이 3: 이분탐색 + accumulate 활용
from itertools import accumulate
from bisect import bisect_right
def solution(d, budget):
    return bisect_right(list(accumulate(sorted(d))), budget)