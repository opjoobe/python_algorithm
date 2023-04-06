# Leetcode # 1089. Duplicate Zeros

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        limit = len(arr)
        i = 0
        while i < limit - 1:
            now = arr[i]
            if now == 0:
                arr.insert(i + 1, 0)
                i += 1
            i += 1
        while len(arr) > limit:
            arr.pop()


# 66ms (beats 87.54%)
