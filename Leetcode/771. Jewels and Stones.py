# Leetcode # 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        answer = 0
        for stone in stones:
            if stone in jewels:
                answer += 1
        return answer

# 30ms (beats 84.50% s)