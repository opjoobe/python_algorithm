# Leetcode # 1629. Slowest Key

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        before_time = max_duration = 0
        answer = ''
        for now_time, now_key in zip(releaseTimes, keysPressed):
            now_duration = now_time - before_time
            before_time = now_time
            if now_duration < max_duration:
                continue
            if now_duration > max_duration:
                answer = now_key
                max_duration = now_duration
            if answer < now_key:
                answer = now_key
        return answer