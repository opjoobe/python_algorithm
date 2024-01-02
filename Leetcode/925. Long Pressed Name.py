# Leetcode # 925. Long Pressed Name

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0] or len(name) > len(typed):
            return False

        before = name[0]
        i = j = 1

        while i < len(name):
            while j < len(typed) and typed[j] != name[i]:
                if typed[j] != before:
                    return False
                j += 1
            before = name[i]
            i += 1
            j += 1

        while j < len(typed) and typed[j] == before:
            j += 1

        return i == len(name) and j == len(typed)