# Leetcode # 217. Contains Duplicate

''' Sol 1 '''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = set()
        for num in nums:
            if num in checked:
                return True
            checked.add(num)
        return False

''' Sol 2 '''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))