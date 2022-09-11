# BOJ # 14681 # 사분면고르기
import sys
input = sys.stdin.readline
x = int(input())
y = int(input())

def quadrant(x,y):
    if x * y > 0:
        return 1 if x > 0 else 3
    return 2 if x < 0 else 4

print(quadrant(x,y))