# Leetcode # 2965. Find Missing and Repeated Values

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        candidates = {x for x in range(1, len(grid) ** 2 + 1)}
        answer = []
        for row in grid:
            for num in row:
                if num in candidates:
                    candidates.remove(num)
                else:
                    answer.append(num)
        answer.append(candidates.pop())
        return answer

# 107ms (beats 99.08%)