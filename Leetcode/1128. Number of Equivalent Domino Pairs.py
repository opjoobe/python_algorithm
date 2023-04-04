# Leetcode # 1128. Number of Equivalent Domino Pairs

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        visited = set()
        overlapped = dict()

        for a, b in dominoes:
            new_domino = str(a) + str(b) if a < b else str(b) + str(a)
            if new_domino not in visited:
                visited.add(new_domino)
            else:
                if new_domino not in overlapped:
                    overlapped[new_domino] = 2
                else:
                    overlapped[new_domino] += 1

        return sum([(cnt - 1) * cnt // 2 for cnt in overlapped.values()])

# 225ms (beats 97.86%)