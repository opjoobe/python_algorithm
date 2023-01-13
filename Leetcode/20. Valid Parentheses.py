# Leetcode # 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {k:v for k,v in zip('(){}[]', [-1,1,-2,2,-3,3])}
        stack = []
        for now_key in s:
            now_val = parentheses[now_key]
            if now_val < 0:
                stack.append(now_val)
                continue
            if not stack or stack[-1] != -now_val: return False
            stack.pop()
        return True if not stack else False

# 32ms (beats 83.99%) 