# Leetcode # 1512. Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        info = collections.Counter(nums)
        answer = 0
        for num, cnt in info.most_common(len(info)):
            if cnt == 1:
                break
            answer += cnt * (cnt - 1) // 2
        return answer