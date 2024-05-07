# Leetcode # 3136. Valid Word

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        
        vowels = set('aeiouAEIOU')
        alphas = set()
        for letter in word:
            if not letter.isalnum():
                return False
            if letter.isalpha():
                alphas.add(letter)
                
        if alphas.difference(vowels) and alphas.intersection(vowels):
            return True
        return False
