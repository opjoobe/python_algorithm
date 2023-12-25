# Leetcode # 2729. Check if The Number is Fascinating

class Solution:
    def isFascinating(self, n: int) -> bool:
        if n > 333:
            return False
        res = set(str(n) + str(n * 2) + str(n * 3))
        if '0' in res or len(res) != 9:
            return False
        return True

