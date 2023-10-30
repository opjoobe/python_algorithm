# Leetcode # 1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        final_sum, final_product = 0, 1
        while n > 0:
            n, rem = divmod(n, 10)
            final_sum += rem
            final_product *= rem
        return final_product - final_sum
        