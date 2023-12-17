# Leetcode # 1710. Maximum Units on a Truck

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        answer = 0
        limit = truckSize
        for box, unit in boxTypes:
            if limit > box:
                limit -= box
                answer += box * unit
            else:
                answer += limit * unit
                break
        return answer
        