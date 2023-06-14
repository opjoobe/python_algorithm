# Leetcode # 485. Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, max_cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
        return max(max_cnt, cnt)