# Leetcod # 1160. Find Words That Can Be Formed by Characters

from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        source = Counter(chars)
        answer = 0
        for word in words:
            for char, count in Counter(word).items():
                if char not in source or source[char] < count:
                    break
            else:
                answer += len(word)
        return answer
    
# 152ms (beats 68.18%)
