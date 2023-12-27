# Leetcode # 1880. Check if Word Equals Summation of Two Words

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        converter = dict(zip("abcdefghij", "0123456789"))
        firstnum = "".join([converter[letter] for letter in firstWord])
        secondnum = "".join([converter[letter] for letter in secondWord])
        targetnum = "".join([converter[letter] for letter in targetWord])
        return int(targetnum) == int(firstnum) + int(secondnum)
        