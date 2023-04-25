# Leetcode # 1588. Sum of All Odd Length Subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        n = len(arr)
        for oddlen in range(1, n + 1, 2):
            for last in range(oddlen, n + 1):
                result += sum(arr[last - oddlen : last])
        return result

# 58ms (beats 64.39%)