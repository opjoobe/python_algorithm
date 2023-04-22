# Leetcode # 1394. Find Lucky Integer in an Array

from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for num, cnt in Counter(arr).most_common(len(arr)):
            if num == cnt:
                return num
        return -1

# 51 ms (beats 94.82 %)

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_dict = dict()
        impossible = set()
        candidate = set()
        for num in arr:
            if num in impossible:
                continue
            if num not in num_dict:
                num_dict[num] = 0
            elif num_dict[num] == num:
                candidate.remove(num)
                impossible.add(num)
                del num_dict[num]
                continue
            num_dict[num] += 1
            if num_dict[num] == num:
                candidate.add(num)
        return max(candidate) if candidate else -1

# solution without 'Counter'