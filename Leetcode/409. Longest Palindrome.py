# Leetcode # 409. Longest Palindrome

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        info = Counter(s)
        answer = 0
        mid_flag = False
        for _, cnt in info.most_common(len(info)):
            answer += (cnt // 2) * 2
            if cnt % 2 == 1:
                mid_flag = True
                if cnt == 1:
                    break
        return answer + 1 if mid_flag else answer


