# Leetcode # 2942. Find Words Containing Character

""" Easy one for birthday"""

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [idx for idx, word in enumerate(words) if x in word]

# 55ms (beats 96.43%)