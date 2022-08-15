from sys import stdin
from collections import deque
input = stdin.readline

S = input().strip() # 주어진 문자열
q1 = deque(S) # 주어진 문자열로 스택을 생성
q2 = deque()
M = int(input()) # 입력할 명령어의 개수

for _ in range(M):
    now = input().strip().split()
    order = now[0]
    if order == 'L':
        if not q1:
            continue
        q2.appendleft(q1.pop())
    elif order == 'D':
        if not q2:
            continue
        q1.append(q2.popleft())
    elif order == 'B':
        if not q1:
            continue
        q1.pop()
    else:
        q1.append(now[1])
print(''.join(q1+q2))
