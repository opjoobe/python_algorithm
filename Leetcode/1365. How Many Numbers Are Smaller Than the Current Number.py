# Leetcode # 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        rank = dict()
        for cnt, num in enumerate(sorted(nums)):
            if num not in rank:
                rank[num] = cnt
        return [rank[num] for num in nums]
      
# 55ms (beats 91.8%)
