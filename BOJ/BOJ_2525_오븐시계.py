# BOJ # 2525 # 오븐시계
"""첫째 줄에는 현재 시각이 나온다. 
현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 
두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다. """

import sys
input = sys.stdin.readline
A, B = map(int, input().strip().split())
C = int(input())

print(*divmod((A * 60 + B + C) % 1440, 60))
