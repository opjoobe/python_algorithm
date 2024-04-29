# Leetcode # 3120. Count the Number of Special Characters I

from collections import defaultdict
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letter_dict = defaultdict(set)
        answer = 0
        for letter in word:
            key = letter.lower()
            if len(letter_dict[key]) == 2:
                continue
            letter_dict[key].add(letter)
            if len(letter_dict[key]) == 2:
                answer += 1
        return answer

# 28 ms (beats 95.62% on Runtime, beats 90.76% on Memory Usage)