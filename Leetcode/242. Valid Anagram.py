# Leetcode # 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = sorted(collections.Counter(s).items(), key = lambda x:(x[0], x[1]))
        t_dict = sorted(collections.Counter(t).items(), key = lambda x:(x[0], x[1]))
        return s_dict == t_dict