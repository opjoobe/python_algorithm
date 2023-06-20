# Leetcode # 551. Student Attendance Record I

class Solution:
    def checkRecord(self, s: str) -> bool:
        total_A = 0
        consecutive_L = 0
        for record in s:
            if record == 'L':
                if consecutive_L == 2:
                    return False
                consecutive_L += 1
            else:
                consecutive_L = 0
                if record == 'A':
                    if total_A != 0:
                        return False
                    total_A = 1
        return True
            
