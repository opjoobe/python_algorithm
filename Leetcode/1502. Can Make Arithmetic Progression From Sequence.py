# Leetcode # 1502. Can Make Arithmetic Progression From Sequence

from heapq import heapify, heappop
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        heapify(arr)
        first = heappop(arr)
        before = heappop(arr)
        gap = before - first
        while arr:
            now = heappop(arr)
            if now - before != gap:
                return False
            before = now
        return True