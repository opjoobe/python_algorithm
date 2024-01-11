# Leetcode # 2733. Neither Minimum nor Maximum

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        counter = []
        for num in nums:
            if num in counter:
                continue
            counter.append(num)
            if len(counter) == 3:
                return sorted(counter)[1]
        return -1
