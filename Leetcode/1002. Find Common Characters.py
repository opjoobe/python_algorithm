# Leetcode # Find Common Characters

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        answer = []
        for letter in words.pop():
            for word in words:
                if letter not in word:
                    break
            else:
                answer.append(letter)
                words = [words[i].replace(letter, '', 1) for i in range(len(words))]
        return answer
                
# 48ms (beats 77.58 %)