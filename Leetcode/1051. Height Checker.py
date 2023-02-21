# Leetcode # 1051. Height Checker

class Solution(object):
    def heightChecker(self, heights):
        return sum([h != e for h,e in zip(heights, sorted(heights))])
        
# 23ms (beats 62.53%)
