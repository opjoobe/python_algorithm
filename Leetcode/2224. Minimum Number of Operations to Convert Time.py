# Leetcode # 2224. Minimum Number of Operations to Convert Time

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr_hr, curr_min = map(int, current.split(":"))
        correct_hr, correct_min = map(int, correct.split(":"))
        min_diff = correct_min - curr_min
        answer = correct_hr - curr_hr

        if min_diff < 0:
            min_diff += 60
            answer -= 1

        if min_diff >= 15:
            answer += min_diff // 15
            min_diff %= 15

        if min_diff >= 5:
            answer += min_diff // 5
            min_diff %= 5
            
        answer += min_diff
        return answer
