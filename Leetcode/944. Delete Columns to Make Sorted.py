# Leetcode # 944. Delete Columns to Make Sorted

class Solution(object):
    def minDeletionSize(self, strs):
        answer = 0
        for j in range(len(strs[0])):
            before = ord(strs[0][j])
            for i in range(len(strs)):
                now = ord(strs[i][j])
                if before > now : 
                    answer += 1
                    break
                before = now
        return answer
      
# 116ms (beats 94.70%)
