# Leetcode # 1389. Create Target Array in the Given Order

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = list()
        for now_num, now_idx in zip(nums, index):
            target.insert(now_idx, now_num)
        return target

# 39ms (beats 54.60%)