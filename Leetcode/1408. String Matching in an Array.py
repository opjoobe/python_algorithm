# Leetcode # 1408. String Matching in an Array

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = set()
        for w1 in words:
            for w2 in words:
                if w1 == w2: continue
                if w1 in w2:
                    answer.add(w1)
        return list(answer)

# 39ms (beats 63.99%)