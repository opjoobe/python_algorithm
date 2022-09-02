import sys
input = sys.stdin.readline
N = int(input())
before = [int(input())]
now = []
for i in range(1, N):
    now = list(map(int, input().strip().split()))
    now[0] += before[0]
    now[-1] += before[-1]
    for j in range(1, i):
        now[j] += max(before[j-1], before[j])
    before = now
print(max(now) if len(now) > 0 else before[0])