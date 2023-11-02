# Leetcode # 1544. Make The String Great

class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for letter in s[1:]:
            if stack and abs(ord(stack[-1]) - ord(letter)) == 32:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)