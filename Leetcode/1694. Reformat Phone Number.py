# Leetcode # 1694. Reformat Phone Number

class Solution:
    def reformatNumber(self, number: str) -> str:
        number = re.sub(r' |-', '', number)
        groups = [number[i:i+3] for i in range(0, len(number), 3)]
        last = groups.pop()
        if len(last) == 1:
            last2 = groups.pop()
            last = last2[:2] + '-' + last2[2] + last
        groups.append(last)
        return '-'.join(groups)