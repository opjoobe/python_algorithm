# Leetcode # 1844. Replace All Digits with Characters

class Solution:
    def replaceDigits(self, s: str) -> str:
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        alpha_index = dict(zip(alphas, range(len(alphas))))
        new_s = ''
        for i in range(len(s)//2):
            c, x = s[i * 2], int(s[i * 2 + 1])
            new_s += c + alphas[alpha_index[c] + x]
        if len(s) % 2:
            new_s += s[-1]
        return new_s

# 28ms (beats 87.62%)