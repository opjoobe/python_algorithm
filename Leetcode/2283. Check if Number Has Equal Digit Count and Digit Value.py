# Leetcode # 2283. Check if Number Has Equal Digit Count and Digit Value

from collections import defaultdict
class Solution:
    def digitCount(self, num: str) -> bool:
        counter = defaultdict(int)
        for i in num:
            counter[int(i)] += 1
        
        for idx, cnt in enumerate(num):
            if counter[idx] != int(cnt):
                print(idx, counter[idx], int(cnt))
                return False

        return True