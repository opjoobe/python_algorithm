# Leetcode # 3074. Apple Redistribution into Boxes

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)
        for i, now_apple in enumerate(sorted(capacity, reverse=True), 1):
            total_apple -= now_apple
            if total_apple <= 0:
                return i
        return len(capacity)
