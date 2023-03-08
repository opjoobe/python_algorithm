# Leetcode # 1913. Maximum Product Difference Between Two Pairs

from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        w = x = 0
        y = z = 10 ** 4 + 1
        for num in nums:
            if num < y:
                y = num
                if y < z:
                    y, z = z, y
            if num > x:
                x = num
                if x > w:
                    w, x = x, w
        return w * x - y * z
        
# 155 ms (beats 99.66 %)