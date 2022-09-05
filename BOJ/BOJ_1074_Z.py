# 백준 1074번 Z

import sys

N, R, C = map(int, sys.stdin.readline().strip().split())

def Z(n, r, c):
    if n == 0:
        return 0
    adder = 2 ** ((n-1) * 2)
    half = 2 ** (n-1)
    if r < half:
        if c < half:
            return adder * 0 + Z(n-1,r,c)
        else:
            return adder * 1 + Z(n-1,r,c-half)
    else:
        if c < half:
            return adder * 2 + Z(n-1,r-half,c)
        else:
            return adder * 3 + Z(n-1, r-half, c-half)

print(Z(N,R,C))