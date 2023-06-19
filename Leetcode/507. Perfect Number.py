# Leetcode # 507. Perfect Number

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        div_sum = 1
        bound = num ** 0.5
        flag = True if bound % 1 == 0 else False
        for i in range(2, int(bound) + 1):
            if num % i == 0:
                div_sum += (i + num // i)
        if flag:
            div_sum -= int(bound)
        return div_sum == num
