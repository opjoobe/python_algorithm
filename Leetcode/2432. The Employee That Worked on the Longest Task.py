# Leetcode # 2432. The Employee That Worked on the Longest Task

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        before = max_duration = 0
        answer = -1
        for worker, now in logs:
            now_duration = now - before
            before = now
            if now_duration < max_duration:
                continue
            if now_duration == max_duration and answer < worker:
                continue
            max_duration = now_duration
            answer = worker
        return answer