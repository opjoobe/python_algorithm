# Leetcode # 290. Word Pattern

import re
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letters_in_pattern = dict()
        words = s.split()
        for idx, letter in enumerate(pattern):
            if letter in letters_in_pattern: continue
            letters_in_pattern[letter] = idx
        for letter, idx in letters_in_pattern.items():
            word = words[idx]
            s = re.sub(word, str(ord(letter)), s)
        s = re.sub('w+', lambda x: chr(int(x)), s)
        print(re.sub(' ', '', s))
        return re.sub(' ', '', s) == pattern