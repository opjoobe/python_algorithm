# Leetcode # 1920. Build Array from Permutation

class Solution(object):
    def buildArray(self, nums):
        nums_info = dict(enumerate(nums))
        return [nums_info[num]for num in nums]
        
# 89ms (beats 89.41%)
