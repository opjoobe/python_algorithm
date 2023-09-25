# Leetcode # 1446. Consecutive Characters

class Solution:
    def maxPower(self, s: str) -> int:
        now = s[0]
        answer = cnt = 1
        for character in s[1:]:
            if character == now:
                cnt += 1
                continue
            answer = max(answer, cnt)
            now = character
            cnt = 1
        return max(answer, cnt)
        