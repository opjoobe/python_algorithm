# Leetcode # 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        x_str = str(x)
        n = len(x_str) // 2
        left, right = n - 1 , n
        if len(x_str) % 2 != 0: right += 1
        for i in range(n):
            if x_str[left] != x_str[right]: return False
            left, right = left - 1, right + 1
        return True

# 68ms (beats 77.5%), 13.8 MB (beats 96.8%)