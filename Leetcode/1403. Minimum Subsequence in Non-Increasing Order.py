# Leetcode # 1403. Minimum Subsequence in Non-Increasing Order

class Solution(object):
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        left, right = 0, len(nums) - 1
        total = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            now_sum = sum(nums[ : mid + 1])
            if now_sum > total - now_sum:
                right = mid - 1 
            else:
                left = mid + 1
        return nums[:left + 1]
