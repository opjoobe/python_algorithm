# 프로그래머스 # 완전탐색 # 소수찾기
from itertools import permutations
def solution(numbers):
    n = len(numbers)
    all_set = set()
    for i in range(1, n+1):
        for case in permutations(numbers, i):
            all_set.add(int(''.join(case)))
    end = max(all_set)
    is_prime = [False] * 2 + [True] * end
    for num in range(2, int(end ** 0.5) + 1):
        if is_prime[num]:
            for next_num in range(num * num, end + 1, num):
                is_prime[next_num] = False
    return len([num for num in all_set if is_prime[num]])