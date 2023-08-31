# Leetcode # 198. House Robber

''' Solution 1 : DP '''
class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP[i] = max(DP[i-2] + nums[i], DP[i-1])
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i, num in enumerate(nums[1:], 2):
            dp[i] = max(dp[i-1], dp[i-2] + num)
        return dp[len(nums)]
    
''' Solution 2 : Reuse original List '''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[:2])
        for i, num in enumerate(nums[2:], 2):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        return nums[-1]
    
''' Solution 3 : use variables instead of List '''
class Solution:
    def rob(self, nums: List[int]) -> int:
        ahead2, ahead1 = 0, nums[0]
        for num in nums[1:]:
            ahead2, ahead1 = ahead1, max(ahead2 + num, ahead1)
        return ahead1
