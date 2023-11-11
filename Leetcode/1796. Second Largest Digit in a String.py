# Leetcode # 1796. Second Largest Digit in a String

class Solution:
    def secondHighest(self, s: str) -> int:
        digits = sorted(set([letter for letter in s if letter.isdigit()]), reverse=True)
        return int(digits[1]) if len(digits) > 1 else -1