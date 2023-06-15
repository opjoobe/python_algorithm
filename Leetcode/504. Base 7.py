# Leetcode # 504. Base 7

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        flag = False
        if num < 0:
            num = -num
            flag = True
        ans = ''
        while num != 0:
            num, now = divmod(num, 7)
            ans = str(now) + ans
        return "-" + ans if flag else ans