# Leetcode # 500. Keyboard Row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1, s2, s3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        answer = []
        for word in words:
            now_s = set(word.lower())
            for s in (s1, s2, s3):
                if not now_s.difference(s):
                    answer.append(word)
                    break
        return answer