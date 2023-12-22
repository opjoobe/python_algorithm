# Leetcode # 2287. Rearrange Characters to Make Target String

from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_info, target_info = Counter(s), Counter(target)
        answer = len(s)
        for letter, cnt in target_info.items():
            now = s_info.get(letter, 0) // cnt
            if now >= answer:
                continue
            answer = now
            if answer == 0:
                return 0
        return answer       