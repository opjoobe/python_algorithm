# Leetcode # 1200. Minimum Absolute Difference

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        before = arr[1]
        mindiff = arr[1] - arr[0]
        answer = [[arr[0], arr[1]]]
        for now in arr[2:]:
            nowpair = [before, now]
            nowdiff = now - before
            before = now
            if nowdiff > mindiff: continue
            if nowdiff < mindiff:
                mindiff = nowdiff
                answer.clear()
            answer.append(nowpair)
        return answer