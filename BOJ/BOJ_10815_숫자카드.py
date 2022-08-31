#백준 #10815 #숫자카드

# 간단히 집합(set) 활용
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

# 이분탐색 활용
import sys
input = sys.stdin.readline
N = int(input())
cards = sorted(map(int, set(input().strip().split())))
M = int(input())
intList = list(map(int, input().strip().split()))
total = len(cards)
for nowNum in intList:
    start = 0
    end = total-1 # 이걸 total로 하면 indexError 발생. start가 계속 커지다가 end랑 같아지는 경우도 생기기 때문 # 
    flag = False
    while start <= end:
        mid = (start + end) // 2
        nowCheck = cards[mid]
        if nowCheck == nowNum:
            flag = True
            break
        elif nowCheck > nowNum:
            end = mid - 1
        else:
            start = mid + 1
    print(1 if flag else 0, end = ' ')