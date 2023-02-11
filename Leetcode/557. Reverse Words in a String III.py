# Leetcode # 557. Reverse Words in a String III.py


class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        for idx in range(len(s)):
            s[idx] = s[idx][::-1]
        return ' '.join(s)
