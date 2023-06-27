# Leetcode # 495. Teemo Attacking

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        start = timeSeries[0]
        end = start + duration
        total = 0
        for sec in timeSeries[1:]:
            if sec > end:
                total += end - start
                start = sec
            end = sec + duration
        total += end - start
        return total
