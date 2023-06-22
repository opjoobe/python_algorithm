# Leetcode # 520. Detect Capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.istitle() or word.islower()
    
'''
isupper() : check if the word is consist of uppercases only
islower() : check if the word is consist of lowercases only
istitle() : check if only the first letter of word is uppercase, and the others are lowercases.
'''