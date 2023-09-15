# Leetcode # 1450. Number of Students Doing Homework at a Given Time

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return len([1 for start, end in zip(startTime, endTime) if start <= queryTime <= end])
        