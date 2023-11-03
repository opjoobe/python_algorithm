# Leetcode # 1556. Thousand Separator

class Solution:
    def thousandSeparator(self, n: int) -> str:
        str_n = str(n)
        if len(str_n) <= 3:
            return str_n
        start = len(str_n) % 3
        answer = "" if start == 0 else str_n[:start] + "."
        answer += ".".join([str_n[i:i+3] for i in range(start, len(str_n), 3)])
        return answer
        