# Leetcode # 819. Most Common Word

from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pattern = re.compile('\w+')
        words = re.findall(pattern, paragraph.lower())
        for word, _ in Counter(words).most_common(len(words)):
            if word not in banned:
                return word

# 27ms (beats 98.61%)