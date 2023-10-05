# Leetcode # 1614. Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = collections.deque()
        answer = 0
        for char in s:
            if char == "(":
                stack.append(1)
                answer = max(answer, len(stack))
            elif char == ")":
                stack.pop()
        return answer