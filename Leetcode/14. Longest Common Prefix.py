# Leetcode # Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        before = strs[0]
        for now in strs[1:]:
            end = min(len(before), len(now))
            before = before[:end]
            for idx in range(end):
                if before[idx] != now[idx]:
                    before = before[:idx]
                    break
            if not before: return ""
        return before

# 36ms (beats 82.38%)