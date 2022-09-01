# BOJ # 2212 # 센서
import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
sensors = sorted(set(map(int, input().strip().split())))
diffs = list()
total = sensors[-1] - sensors[0]

before = sensors.pop(0)
for now in sensors:
    diffs.append(now - before)
    before = now

diffs.sort(reverse=True)

answer = sum(diffs[K-1:])
print(answer)
