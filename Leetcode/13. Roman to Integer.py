# Leetcode # 13. Roman to Integer

from collections import Counter
import re
class Solution:
    def romanToInt(self, s: str) -> int:
        answer_dict = dict()
        roman = {symbol:value for symbol,value in zip('IVXLCDM', [1,5,10,50,100,500,1000])}
        for edge_symbol, value in zip(['IV','IX','XL','XC','CD','CM'], [4,9,40,90,400,900]):
            roman[edge_symbol] = value
        def edge_replace(m): 
            answer_dict[m.group()] = 1
            return ''
        s = re.sub('CM|CD|XC|XL|IX|IV',edge_replace,s)
        answer_dict.update(dict(Counter(s)))
        answer = 0
        for k, v in answer_dict.items():
            answer += roman[k] * v
        return answer

# 59ms (beats 65.24%)