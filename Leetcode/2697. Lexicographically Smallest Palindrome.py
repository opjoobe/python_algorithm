# Leetcode # 2697. Lexicographically Smallest Palindrome

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        results = []
        for i in range(len(s) // 2):
            results.append(sorted([s[i], s[-i-1]])[0])
        mid = [s[len(s) // 2]] if len(s) % 2 != 0 else []
        return ''.join(results + mid + results[::-1])
    