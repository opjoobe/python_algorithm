# Leetcode # 2960

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        answer = 0
        for i in range(n):
            if batteryPercentages[i] <= 0:
                continue
            answer += 1
            cnt = 0
            for j in range(i + 1, n):
                if batteryPercentages[j] > 0:
                    cnt += 1
                    batteryPercentages[j] -= 1
            if cnt == 0:
                break
        return answer
            
        