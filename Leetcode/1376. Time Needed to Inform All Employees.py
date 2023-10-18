# Leetcode # 1376. Time Needed to Inform All Employees

from collections import defaultdict, deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        answer = 0
        children = defaultdict(list)
        for i, parent in enumerate(manager):
            children[parent].append(i)
        q = deque([(headID, 0)])
        while q:
            worker_id, total_time = q.popleft()
            if not children[worker_id]:
                answer = max(answer, total_time)
                continue
            total_time += informTime[worker_id]
            for next_id in children[worker_id]:
                q.append((next_id, total_time))
        return answer