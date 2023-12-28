# Leetcode # 2404. Most Frequent Even Element

from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_info = defaultdict(int)
        candidates = []
        maxi = 0
        for num in nums:
            if num % 2 != 0:
                continue
            even_info[num] += 1
            if maxi > even_info[num]:
                continue
            if maxi < even_info[num]:
                maxi = even_info[num]
                candidates.clear()
            heappush(candidates, num)
        if not candidates:
            return -1
        return heappop(candidates)
        