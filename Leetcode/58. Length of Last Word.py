# Leetcode # 58. Length of Last Word

import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(re.findall('\w+', s)[-1])


# 24ms (beats 97.42%) 