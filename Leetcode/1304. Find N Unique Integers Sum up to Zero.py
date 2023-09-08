# Leetcode # 1304. Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        quo, rem = divmod(n, 2)
        answer = [i for i in range(-quo, quo + 1)]
        if rem == 0:
            answer.remove(0)
        return answer