# Leetcode # 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        target = max(candies) - extraCandies
        return [True if candy >= target else False for candy in candies]