# Leetcode # 1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_counter = collections.Counter(arr)
        return len(arr_counter) == len(set(arr_counter.values()))
        