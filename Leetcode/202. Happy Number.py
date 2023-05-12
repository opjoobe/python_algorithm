# Leetcode # 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {n}
        while True:
            temp = 0
            while n > 0:
                n, now = divmod(n, 10)
                temp += now ** 2
            n = temp
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            