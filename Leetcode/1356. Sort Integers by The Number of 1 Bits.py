# Leetcode # 1356. Sort Integers by The Number of 1 Bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x: (x.bit_count(), x))
    
"""
int.bit_count() returns the number of '1's in binary expression of the given int.

def bit_count(self):
    return bin(self).count('1')
"""
        