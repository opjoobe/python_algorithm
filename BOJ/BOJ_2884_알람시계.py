# BOJ # 2884 # 알람시계
import sys
input = sys.stdin.readline
hour, min = map(int, input().strip().split())

if min >= 45:
    min -= 45
else:
    hour -= 1
    min += 15

if hour < 0:
    hour = 23
print(hour, min)