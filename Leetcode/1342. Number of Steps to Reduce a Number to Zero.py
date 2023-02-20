# Leetcode # 1342. Number of Steps to Reduce a Number to Zero

class Solution(object):
    def numberOfSteps(self, num):
        if num == 0: return 0
        answer = 0
        while num & (num - 1) != 0:
            if num % 2:
                num -= 1
            else:
                num >>= 1
            answer += 1
        answer += len(bin(num)) - 2
        return answer 
      
# 15ms (beats 82.99%)
