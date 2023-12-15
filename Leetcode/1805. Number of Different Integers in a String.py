# Leetcode # 1805. Number of Different Integers in a String

import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = [int(num) for num in re.findall('\d+', word)]
        unique_nums = set(nums)
        return len(unique_nums)