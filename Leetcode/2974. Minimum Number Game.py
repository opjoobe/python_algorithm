# Leetcode # 2974. Minimum Number Game

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        arr = []
        n = len(nums) // 2
        for _ in range(n):
            n1 = nums.pop()
            n2 = nums.pop()
            arr.append(n2)
            arr.append(n1)
        return arr