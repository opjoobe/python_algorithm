# Leetcode # 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        before = answer = 0
        char_map = dict()
        for idx, letter in enumerate(s):
            if letter not in char_map:
                char_map[letter] = idx
                continue
            answer = max(answer, idx - before)
            before = max(before, char_map[letter] + 1)
            char_map[letter] = idx
        return max(answer, len(s) - before)
        
# 62 ms (beats 71.20 %)