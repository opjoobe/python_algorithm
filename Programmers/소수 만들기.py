# 프로그래머스 # 소수 만들기

from itertools import combinations
def solution(nums):
    N = sum(sorted(nums)[-3:])
    isPrime = [False] * 2 + [True] * (N-1)
    for i in range(2, int(N ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i*i, N+1, i):
                isPrime[j] = False
    return len([case for case in combinations(nums, 3) if isPrime[sum(case)]])