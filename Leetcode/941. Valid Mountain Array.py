# Leetcode # 941. Valid Mountain Array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        idx = 0
        while idx < len(arr) - 1 and arr[idx] < arr[idx + 1]:
            idx += 1
            
        top = idx
        if top in (0, len(arr) - 1):
            return False
        
        while idx < len(arr) - 1 and arr[idx] > arr[idx + 1]:
            idx += 1
        
        return True if idx == len(arr) - 1 else False

"""
arr.length <= 1e4 => needs to be in linear time complexity
"""