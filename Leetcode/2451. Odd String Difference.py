# Leetcode # 2451. Odd String Difference

class Solution:
    def oddString(self, words: List[str]) -> str:
        converter = dict(zip('abcdefghijklmnopqrstuvwxyz',range(26)))
        first, second = words[0], words[1]
        diff_1, diff_2 = list(), list()
        
        for j in range(len(first)-1):
            diff_1.append(converter[first[j+1]]-converter[first[j]])
            diff_2.append(converter[second[j+1]]-converter[second[j]])
        
        if diff_1 == diff_2:
            for word in words[2:]:
                for j in range(len(first)-1):
                    now = converter[word[j+1]]-converter[word[j]]
                    if now != diff_1[j]:
                        return word
        else:
            diff_3 = list()
            for j in range(len(first)-1):
                diff_3.append(converter[words[2][j+1]]-converter[words[2][j]])
            if diff_3 == diff_2:
                return first
            else:
                return second
