# Leetcode # 290. Word Pattern

# better solution
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False
        p_dict, w_dict = dict(), dict()
        for idx, pw in enumerate(zip(pattern, words)):
            p, w = pw
            if p not in p_dict: p_dict[p] = idx
            if w not in w_dict: w_dict[w] = idx
            if p_dict[p] != w_dict[w]: return False
        return True
        
# first solution
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        bijection = dict()
        words, used_words = s.split(), set()
        if len(words) != len(pattern): return False
        for idx, letter in enumerate(pattern):
            now_word = words[idx]
            if letter not in bijection:
                if now_word in used_words: return False
                used_words.add(now_word)
                bijection[letter] = now_word
            else:
                if now_word != bijection[letter]: return False
        return True