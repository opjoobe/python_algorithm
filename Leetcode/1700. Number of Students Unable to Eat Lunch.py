# Leetcode # 1700. Number of Students Unable to Eat Lunch

from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        before, idx = len(q), 0
        while q:
            for _ in range(before):
                now = q.popleft()
                if now == sandwiches[idx]:
                    idx += 1
                else:
                    q.append(now)
            if len(q) == before:
                break
            before = len(q)
        return len(q)