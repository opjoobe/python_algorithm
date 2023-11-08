# Leetcode # 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

import re
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, word in enumerate(sentence.split(), 1):
            if re.match(searchWord, word):
                return idx
        return -1
