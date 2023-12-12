# Leetcode # 1684. Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistents = set(allowed)
        return len([True for word in words if set(word).issubset(consistents)])
    