# Leetcode # 1346. Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        curr = set()
        for num in arr:
            if num * 2 in curr or (num % 2 == 0 and num // 2 in curr):
                return True
            curr.add(num)
        return False