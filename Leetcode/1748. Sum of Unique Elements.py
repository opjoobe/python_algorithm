# Leetcode # 1748. Sum of Unique Elements

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = set()
        duplicate = set()
        for num in nums:
            if num in duplicate:
                continue
            if num in unique:
                duplicate.add(num)
            else:
                unique.add(num)
        return sum(unique - duplicate)