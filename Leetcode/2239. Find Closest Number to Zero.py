# Leetcode # 2239. Find Closest Number to Zero

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        answer_set = {nums[0]}
        answer = abs(nums[0])
        for num in nums[1:]:
            distance = abs(num)
            if distance > answer:
                continue
            if distance == answer:
                answer_set.add(num)
            else:
                if num == 0:
                    return 0
                answer = distance
                answer_set = {num}
        return max(answer_set)        