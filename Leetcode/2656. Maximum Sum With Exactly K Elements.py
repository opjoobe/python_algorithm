# Leetcode # 2656. Maximum Sum With Exactly K Elements

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return k * max(nums) + k * (k - 1) // 2
        
"""
max + (max + 1) + (max + 2) + .... + (max + k - 1)

a = max
l = max + k - 1

An = (a + 1) // 2
"""