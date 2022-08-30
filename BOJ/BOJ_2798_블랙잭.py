#백준 #2798번 #블랙잭
import sys
import itertools
input = sys.stdin.readline
N, M = map(int, input().strip().split())
cards = list(map(int, input().strip().split()))

answer = 0

for i in itertools.combinations(cards,3):
  now = sum(i)
  if answer < now <= M:
    answer = now
    if answer == M:
      break
print(answer)
