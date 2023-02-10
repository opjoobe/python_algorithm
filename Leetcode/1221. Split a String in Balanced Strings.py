# Leetcode # 1221. Split a String in Balanced Strings

class Solution(object):
    def balancedStringSplit(self, s):
        num = {"R":1, "L":-1}
        ans = total = 0
        for direction in s:
            total += num[direction]
            if total == 0: ans += 1
        return ans
