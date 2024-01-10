# Leetcode # 2652. Sum Multiples

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        answer = 0
        
        for num in (3,5,7,-15, -21, -35, 105):
            cnt = n // abs(num) # count of num's multiples
            answer += num * cnt * (cnt + 1) // 2
        
        return answer