# Leetcode # 136. Single Number

from heapq import heapify, heappop
from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        heapify(nums)
        before = heappop(nums)
        while nums:
            if heappop(nums) != before:
                return before
            before = heappop(nums)
        return before

# 126ms (beats 97.53%) 