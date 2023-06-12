# Leetcode # 747. Largest Number At Least Twice of Others

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        return nums.index(first) if first >= second * 2 else -1