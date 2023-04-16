# Leetcode # 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_checked = set()
        for s_now, t_now in zip(s,t):
            if s_now in s_dict and s_dict[s_now] != t_now:
                return False
            if s_now not in s_dict:
                if t_now in t_checked:
                    return False
                s_dict[s_now] = t_now
                t_checked.add(t_now)
        return True