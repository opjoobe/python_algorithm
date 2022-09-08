# BOJ # 3190 # 뱀

from sys import stdin
from collections import deque
input = stdin.readline
import sys
N = int(input())
K = int(input())
apples = [list(map(int, input().strip().split())) for _ in range(K)]
L = int(input())
turns = dict()
for _ in range(L):
    time, direction = input().strip().split()
    turns[int(time)] = direction

directions = [[0,1], [1,0], [0,-1], [-1,0]]
i = 0 # L :  (i+3) % 4 # R : (i+1) % 4

snake = deque()
snake.append([1,1]) # start
t = 0
x,y = 1,1
while True:
    dx, dy = directions[i]
    t += 1
    x += dx
    y += dy
    # 자기 몸이랑 부딪히는 경우
    if [x,y] in snake:
        break
    # 벽이랑 부딪히는 경우
    if not 0 < x <= N or not 0 < y <= N:
        break
    # 머리를 다음칸에 위치시키기
    snake.append([x,y]) 
    # 사과를 먹어 없애고 꼬리를 유지하는 경우
    if [x,y] in apples:
        apples.remove([x,y])
    # 꼬리 위치를 옮기는 경우
    else:
        snake.popleft()
    # 방향 전환을 할 시간인 경우
    if t in turns.keys():
        direction = turns[t]
        if direction == 'D':
            i = (i+1) % 4
        else:
            i = (i+3) % 4
print(t)

    

