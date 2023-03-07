# Leetcode # 1816. Truncate Sentence

''' Solution 1'''
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split(' ', k)[ : k])

# 32ms (beats 61.84%)

''' Solution 2'''
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        answer = ''
        for letter in s:
            if letter == ' ':
                k -= 1
                if k == 0:
                    break
            answer += letter
        return answer

# 26ms (beats 92.7%)