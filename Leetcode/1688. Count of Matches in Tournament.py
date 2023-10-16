# Leetcode # 1688. Count of Matches in Tournament

class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        cnt = 1
        while n > 2:
            n, rest = divmod(n, 2)
            cnt += n
            if rest:
                n += 1
        return cnt
        