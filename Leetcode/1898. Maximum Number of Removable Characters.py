# Leetcode # Maximum Number of Removable Characters # Nexon 과 비슷한 문제

from typing import List
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        s_len, p_len = len(s), len(p)
        remove = {r:i for i,r in enumerate(removable)}
        start, end = 0, len(removable)
        while start <= end:
            mid = (start + end) // 2
            i = -1
            j = 0
            while i < s_len - 1 and j < p_len:
                i += 1
                if i in remove and remove[i] < mid:
                    continue
                if s[i] == p[j]:
                    j += 1
            if j == p_len:
                start = mid + 1
            else:
                end = mid - 1
        return end