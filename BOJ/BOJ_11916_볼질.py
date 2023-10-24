# BOJ # 11916 # 볼질

import sys
input = sys.stdin.readline
N = int(input())
answer = balls = 0
runners = [1, 0, 0, 0]
for now in input().strip().split():
    balls += 1
    if now == '1' and balls < 4:
        continue
    if now != '3':
        balls = 0
        one, two, three = runners[1], runners[2], runners[3]
        runners[1] = 1
        if one != 1:
            continue
        runners[2] = 1
        if two != 1:
            continue
        runners[3] = 1
        if three != 1:
            continue
        answer += 1
    else:
        if runners[3] == 1:
            answer += 1
        runners[3], runners[2], runners[1] = runners[2], runners[1], 0
        if balls == 4:
            runners[1] = 1
            balls = 0
print(answer)
        