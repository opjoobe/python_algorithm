# Leetcode # 2000. Reverse Prefix of Word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        point, wordlen = word.find(ch), len(word)
        return word[-wordlen+point: -wordlen-1:-1] + word[point+1:]
