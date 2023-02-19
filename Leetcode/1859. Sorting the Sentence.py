# Leetcode # 1859. Sorting the Sentence

import re
class Solution(object):
    def sortSentence(self, s):
        return re.sub('\d','',' '.join(sorted(s.split(), key = lambda x: int(x[-1]))))
        
# 11ms (beats 93.49%)
