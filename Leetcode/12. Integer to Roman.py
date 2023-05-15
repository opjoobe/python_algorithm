# Leetcode # 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {value:symbol for value,symbol in zip([1,5,10,50,100,500,1000], 'IVXLCDM')}
        roman.update(dict(zip([4,9,40,90,400,900], ['IV','IX','XL','XC','CD','CM'])))
        answer = ''
        for value, symbol in sorted(roman.items(), reverse = True):
            quotient, num = divmod(num, value)
            if quotient == 0: continue
            answer += quotient * symbol
        return answer