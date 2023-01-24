# Leetcode # 125. Valid Palindrome

import re
''' Solution 1 '''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub('[^a-zA-Z0-9]','',s).lower()
        n = len(new_s)
        left, right = - ((n + 1) // 2 + 1), (n + 1) // 2
        for _ in range(len(new_s) // 2):
            if new_s[left].lower() != new_s[right].lower(): return False
            left, right = left - 1, right + 1
        return True

# 50ms (beats 72.26%)

''' Solution 2 '''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub('[^a-zA-Z0-9]','',s).lower()
        return new_s == new_s[::-1]

# 38ms (beats 96.10%)

''' Solution 3 '''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub('[^a-zA-Z0-9]','',s).lower()
        n = len(new_s)
        left, right = - ((n + 1) // 2 + 1), (n + 1) // 2
        return new_s[left : - n - 1 : -1] == new_s[right: ]

# 36ms (beats 97.50%)