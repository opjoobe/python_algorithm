# Leetcode # 1422. Maximum Score After Splitting a String

class Solution:
    def maxScore(self, s: str) -> int:
        score = s[1:].count('1') + int(s[0] == '0')
        answer = score
        for now in s[1:-1]:
            if now == '0':
                score += 1
                answer = max(answer, score)
            else:
                score -= 1
        return answer
        