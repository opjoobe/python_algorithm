# Leetcode # 3019. Number of Changing Keys

class Solution:
    def countKeyChanges(self, s: str) -> int:
        answer = 0
        before_key = s[0].lower()
        for now in s[1:]:
            now_key = now.lower()
            if now_key == before_key:
                continue
            answer += 1
            before_key = now_key
        return answer