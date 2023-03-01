# Leetcode # 1399. Count Largest Group.py

from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sum = {0: 0}
        curr_dict = defaultdict(int) # check current location of sum (1,2,...,36)
        ans_dict = defaultdict(int) # check the size of groups per each sum (1,2,...,36)
        for num in range(1, n + 1):
            quodient, remainder =  divmod(num, 10)
            res = digit_sum[num] = digit_sum[quodient] + remainder
            curr_dict[res] += 1
            ans_dict[curr_dict[res]] += 1
        return ans_dict[len(ans_dict)]


# 69 ms (beats 92.95%)