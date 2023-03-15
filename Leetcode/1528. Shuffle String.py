# Leetcode # 1528. Shuffle String

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle = dict(zip(indices, s))
        return ''.join([shuffle[i] for i in range(len(s))])

# 52ms (beats 87.46%)