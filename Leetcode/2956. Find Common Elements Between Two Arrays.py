# Leetcode # 2956. Find Common Elements Between Two Arrays

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_info = set(nums1)
        nums2_info = set(nums2)
        
        first = len([True for num in nums1 if num in nums2_info])
        second = len([True for num in nums2 if num in nums1_info])
        return [first, second]

