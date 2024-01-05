# Leetcode # 2678. Number of Senior Citizens

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([True for detail in details if int(detail[11:13]) > 60])
        
"""
used slice method of Python's list, and compare with Integer 60.
"""