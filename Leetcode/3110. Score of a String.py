# Leetcode # 3110. Score of a String

class Solution:
    def scoreOfString(self, s: str) -> int:
        ''' configure score_dict instead of using ord() '''
        score_dict = dict(zip('abcdefghijklmnopqrstuvwxyz', range(26)))
        before = score_dict[s[0]]
        total = 0
        for letter in s[1:]:
            now = score_dict[letter]
            total += abs(before-now)
            before = now
        return total