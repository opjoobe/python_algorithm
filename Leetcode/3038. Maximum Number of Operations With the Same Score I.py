# Leetcode # 3038. Maximum Number of Operations With the Same Score I

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0] + nums[1]
        answer = 1
        idx = 2
        limit = len(nums) - 1
        while idx < limit and (nums[idx] + nums[idx+1]) == score:
            idx += 2
            answer += 1
        return answer

# beats 95.58% on Runtime, beats 92.76% on Memory Usage