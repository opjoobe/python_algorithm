# Leetcode # 66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i, n = -1, -len(digits)
        while i >= n:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        return [1] + digits
      
# 28ms (beats 95.74%)
