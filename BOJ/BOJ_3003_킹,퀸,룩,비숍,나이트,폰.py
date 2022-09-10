# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 
import sys
input = sys.stdin.readline
print(*[y-x for x,y in zip(list(map(int, input().strip().split())), [1,1,2,2,2,8])])
