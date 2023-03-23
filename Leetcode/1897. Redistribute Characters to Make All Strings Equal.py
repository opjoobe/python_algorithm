# Leetcode # 1897. Redistribute Characters to Make All Strings Equal

from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        for letter, cnt in Counter(''.join(words)).items():
            if cnt % n != 0:
                return False
        return True
            
# 47ms (beats 92.81 %)