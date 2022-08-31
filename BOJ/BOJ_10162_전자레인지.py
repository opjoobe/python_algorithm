# BOJ # 10162 # 전자레인지

import sys
input = sys.stdin.readline
T = int(input())

# A : 300, B : 60, C : 10

def microwave(t):
    if t % 10:
        return -1
    A, t = divmod(t, 300)
    B, t = divmod(t, 60)
    C, t = divmod(t, 10)
    if t:
        return -1
    return f'{A} {B} {C}'

print(microwave(T))