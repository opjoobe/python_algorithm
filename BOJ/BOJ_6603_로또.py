# BOJ # 6603 # 로또

# 풀이 1: combinations 사용하기
import sys, itertools
input = sys.stdin.readline

while True:
    K, *S = map(int, input().strip().split())
    if K == 0:
        break
    for case in itertools.combinations(S, 6):
        print(*case)
    print()

# 풀이 2: DFS 사용하기
def lottoSelect(before, cnt, case):
    if cnt == 6:
        print(*case)
        return
    for i in range(before+1, K):
        lottoSelect(i, cnt+1, case + [S[i]])

import sys
input = sys.stdin.readline
while True:
    K, *S = map(int, input().strip().split())
    if K == 0:
        break
    lottoSelect(-1, 0, [])
    print()
