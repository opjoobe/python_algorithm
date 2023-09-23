# Leetcode # 1323. Maximum 69 Number

class Solution:
    def maximum69Number (self, num: int) -> int:
        numstr = str(num)
        idx = numstr.find('6')
        return int(numstr[:idx] + '9' + numstr[idx+1:]) if idx != -1 else num
                
