#백준 #10815 #숫자카드

#이분탐색 활용
from sys import stdin
input = stdin.readline
N = int(input())
cards = set(map(int, input().strip().split()))
M = int(input())
check = list(map(int, input().strip().split()))

for now in check:
    if now in cards:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
