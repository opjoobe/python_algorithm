# Leetcode # 1470. Shuffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for a,b in zip(nums[:n], nums[n:]):
            answer.extend([a,b])
        return answer
