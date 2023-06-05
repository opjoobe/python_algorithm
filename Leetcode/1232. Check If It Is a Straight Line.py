# Leetcode # 1232. Check If It Is a Straight Line

from heapq import heapify, heappop
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        heapify(coordinates)
        first_x, first_y = heappop(coordinates)
        before_x, before_y = heappop(coordinates)
        # get (y/x)
        valid_x = before_x - first_x
        valid_y = before_y - first_y
        while coordinates:
            now_x, now_y = heappop(coordinates)
            # check if before coordinate and now coordinate has y/x slope
            if valid_x * (now_y - before_y) != (now_x - before_x) * valid_y:
                return False
            before_x, before_y = now_x, now_y
        return True