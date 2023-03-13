# Leetcode # 1103. Distribute Candies to People

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        answer = []
        def get_arithmetic_sequence_sum(a:int, d: int, n: int):
            first = a
            last = a + (n - 1) * d
            return (first + last) * n // 2
        start, end = 0, 10 ** 5
        while start <= end:
            mid = (start + end) // 2
            now = get_arithmetic_sequence_sum(1,1, mid)
            if now > candies:
                end = mid - 1
            else:
                start = mid + 1
        total = get_arithmetic_sequence_sum(1, 1, end)
        rest = candies - total
        turns_per_person, j = divmod(end, num_people)
        for i in range(num_people):
            a = i + 1
            d = num_people
            n = turns_per_person
            if i < j:
                n += 1
            now_candies = get_arithmetic_sequence_sum(a, d, n)
            answer.append(now_candies)
        if rest > 0 : 
            answer[j] += rest
        return answer

# 30 ms (beats 98.72%)

            
