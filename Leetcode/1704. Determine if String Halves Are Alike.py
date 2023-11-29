# Leetcode # 1704. Determine if String Halves Are Alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        middle = len(s) // 2
        a, b = s[:middle], s[middle:]
        return len([True for letter in a if letter in vowels]) == len([True for letter in b if letter in vowels])
    
    