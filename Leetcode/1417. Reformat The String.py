# Leetcode # 1417. Reformat The String

class Solution:
    def reformat(self, s: str) -> str:
        def get_permutation(list1: list, list2: list, is_odd: bool):
            result = ''
            for i, j in zip(list1, list2):
                result += i + j
            if is_odd:
                result += list1[-1]
            return result

        n = len(s)
        limit = n//2 + int(n % 2 != 0)
        digits, alphas = list(), list()
        
        for letter in s:
            if letter.isdigit():
                digits.append(letter)
            else:
                alphas.append(letter)
            if len(digits) > limit or len(alphas) > limit:
                return ""

        if n % 2 != 0:
            if len(digits) == limit:
                answer = get_permutation(digits, alphas, True)
            else:
                answer = get_permutation(alphas, digits, True)
        else:
            answer = get_permutation(digits, alphas, False)
            
        return answer

# 46ms (beats 65.3%)