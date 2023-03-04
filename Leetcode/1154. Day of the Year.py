# Leetcode # 1154. Day of the Year

class Solution:
    def dayOfYear(self, date: str) -> int:
        dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        year, month, day = map(int, date.split('-'))
        if year != 1900 and year % 4 == 0:
            dates[1] = 29
        return sum(dates[ : month - 1]) + day

# 64ms (beats 93.56%)