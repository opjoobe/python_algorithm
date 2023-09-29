# Leetcode # 1773. Count Items Matching a Rule

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx = {"type": 0, "color": 1, "name": 2}[ruleKey]
        cnt = 0
        for item in items:
            if item[idx] == ruleValue:
                cnt += 1
        return cnt