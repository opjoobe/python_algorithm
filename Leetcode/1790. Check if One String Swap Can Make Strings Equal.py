# Leetcode # 1790. Check if One String Swap Can Make Strings Equal

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap = ""
        for idx in range(len(s1)):
            s1_char, s2_char = s1[idx], s2[idx]
            if s1_char != s2_char:
                if not swap:
                    swap = s1_char + s2_char
                elif swap == s2_char + s1_char and s1[idx + 1:] == s2[idx + 1:]:
                    return True
                else:
                    return False
        return swap == ""