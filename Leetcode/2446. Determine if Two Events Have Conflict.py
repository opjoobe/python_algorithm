# Leetcode # 2446. Determine if Two Events Have Conflict

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        new_event1 = [x.split(":") for x in event1]
        new_event2 = [x.split(":") for x in event2]
        hour1, hour2 = new_event1[0][0], new_event2[0][0]
        min1, min2 = new_event1[0][1], new_event2[0][1]
        if hour1 >= hour2:
            if hour1 > hour2 or min1 > min2:
                new_event1, new_event2 = new_event2, new_event1
        if new_event1[1][0] >= new_event2[0][0]:
            if new_event1[1][0] > new_event2[0][0] or new_event1[1][1] >= new_event2[0][1]:
                return True
        return False
        