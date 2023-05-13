# Leetcode # 1046. Last Stone Weight

from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapify(stones)
        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            if x != y:
                heappush(stones, x - y)
        return -stones[0] if stones else 0

