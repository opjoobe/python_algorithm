# Leetcode # 1175. Prime Arrangements

from math import factorial
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        is_prime = [0] * 2 + [1] * (n - 1)
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i] == 0:
                continue
            for j in range(i*i, n+1, i):
                is_prime[j] = 0
        prime_cnt = sum(is_prime)

        non_prime_permutation_cnt = factorial(n - prime_cnt) % (10 ** 9 + 7)
        prime_permutation_cnt = factorial(prime_cnt) % (10 ** 9 + 7)

        return non_prime_permutation_cnt * prime_permutation_cnt % (10 ** 9 + 7)

# 28ms (beats 90.4%)