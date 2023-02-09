# Leetcode # 1662. Check If Two String Arrays are Equivalent

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1) == ''.join(word2)
