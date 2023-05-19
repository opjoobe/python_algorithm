# Leetcode # 344.Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        ''' Solution 1 : Use Two Pointer'''
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

        ''' Solution 2 : Pythonic way'''
        s.reverse()
        