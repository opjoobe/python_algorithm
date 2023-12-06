# Leetcode # 2951. Find the Peaks

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        answer = []
        before = mountain[0]
        for i in range(1, len(mountain) - 1):
            now = mountain[i]
            if before < now and mountain[i+1] < now:
                answer.append(i)
            before = now
        return answer
