# 프로그래머스 # 숫자 카드 나누기

from functools import reduce
from math import gcd
def solution(arrayA, arrayB):
    def get_a(L1, L2):
        gcd_L1 = reduce(gcd, L1, L1[0]) # repeat gcd() by iterating L1, with L1[0] as an initial value.
        candidates = {gcd_L1} 
        for num in range(2, int(gcd_L1 ** 0.5) + 1):
            num2, rest = divmod(gcd_L1, num)
            if not rest: candidates.update([num, num2])
        for candidate in sorted(candidates, reverse = True): # get the biggest candidate fulfills the given condition.
            for num in L2:
                if num % candidate == 0: break
            else:
                return candidate
        return 0 # if there isn't any candidate available as 'a', just return zero.
    return max(get_a(arrayA, arrayB), get_a(arrayB, arrayA)) 