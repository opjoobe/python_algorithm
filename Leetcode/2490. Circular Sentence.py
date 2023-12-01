# Leetcode # 2490. Circular Sentence

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        before = words[0][-1]
        for word in words[1:]:
            if word[0] != before:
                return False
            before = word[-1]
        return True if before == words[0][0] else False