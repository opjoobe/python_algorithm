# Leetcode # 1385. Find the Distance Value Between Two Arrays

from bisect import bisect_right
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        visited = dict()
        def check_valid(num: int) -> bool:
            if num in visited:
                return visited[num]
            val = True
            result = bisect_right(arr2, num)
            if result == len(arr2):
                # check last one
                if abs(num - arr2[-1]) <= d:
                    val = False
            elif result == 0:
                # check first one
                if abs(num - arr2[0]) <= d:
                    val = False
            else:
                left, right = arr2[result - 1], arr2[result]
                if abs(num - left) <= d or abs(num - right) <= d:
                    val = False
            visited[num] = val
            return val
        answer = 0
        for num in arr1:
            if check_valid(num):
                answer += 1
        return answer

# 77ms (beats 87.72%)