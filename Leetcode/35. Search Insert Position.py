# Leetcode # Search Insert Position

from typing import *
from bisect import bisect_left
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target) # check the insert position

# 50ms (beats 88.61%) 