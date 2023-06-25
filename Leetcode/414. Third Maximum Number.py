# Leetcode # 414. Third Maximum Number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = [-num for num in set(nums)]
        if len(s) < 3:
            return -min(s)
        heapq.heapify(s)
        for _ in range(3):
            answer = heapq.heappop(s)
        return -answer
    
'''
heapify : build heap in O(N)
=> useful when we need only few maximum / minimum numbers
'''