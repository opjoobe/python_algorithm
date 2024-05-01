# Leetcode # 3114. Latest Time You Can Obtain After Replacing Characters

class Solution:
    def findLatestTime(self, s: str) -> str:
        s_list = list(s)
        
        if s_list[0] == "?":
            s_list[0] = "1" if s_list[1] in {"0","1","?"} else "0"
            
        if s_list[1] == "?":
            s_list[1] = "1" if s_list[0] == "1" else "9"
            
        if s_list[3] == "?":
            s_list[3] = "5"
            
        if s_list[4] == "?":
            s_list[4]= "9"
            
        return ''.join(s_list)
    
# 25ms (beats 98.51% on Runtime, beats 95.08% in Memory Usage)