# Leetcode # 1437. Check If All 1's Are at Least Length K Places Away

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        now = len(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                now = i
                break
        before = now
        now += 1
        while now < len(nums):
            if nums[now] == 1:
                if now - before - 1 < k:
                    return False
                before = now
            now += 1
        return True
    
# runtime: 458ms (beats 99.02%)