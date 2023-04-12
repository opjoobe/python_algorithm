# Leetcode # 1380. Lucky Numbers in a Matrix

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        maxi = 10 ** 5
        m, n = len(matrix), len(matrix[0])
        min_rows = dict([(row, (maxi, 0)) for row in range(m)])
        min_cols = dict([(col, 0) for col in range(n)])
        # needs both idx and value
        for row in range(m):
            for col in range(n):
                now = matrix[row][col]
                if min_rows[row][0] > now:
                    min_rows[row] = (now, col)
                if min_cols[col] < now:
                    min_cols[col] = now
        answer = []
        for val, col in min_rows.values():
            if val == min_cols[col]:
                answer.append(val)
        return answer

# 129 ms (beats 73.46 %)