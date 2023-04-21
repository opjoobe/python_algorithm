# Leetcode # 1394. Find Lucky Integer in an Array

from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for num, cnt in Counter(arr).most_common(len(arr)):
            if num == cnt:
                return num
        return -1

# 51 ms (beats 94.82 %)