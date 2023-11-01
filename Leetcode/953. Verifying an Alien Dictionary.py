# Leetcode # 953. Verifying an Alien Dictionary

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_to_human = dict(zip(order, 'abcdefghijklmnopqrstuvwxyz'))
        return words == sorted(words, key = lambda word: ''.join(alien_to_human[letter] for letter in word))
    