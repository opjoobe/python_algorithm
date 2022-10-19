# BOJ # 1963 # 소수 경로

from sys import stdin
from collections import deque, defaultdict
# 1 . 우선 4자리 숫자 중에 소수 여부부터 정하기
is_prime = [True] * 10001
for num in range(2, 101):
    if is_prime[num]:
        for next_num in range(num * num, 10001, num):
            is_prime[next_num] = False
# 2 . A -> B 체크
input = stdin.readline
for _ in range(int(input())):
    A, B = input().strip().split()
    if A == B:
        print(0)
        continue
    checked = defaultdict(int)
    q = deque([A])
    checked[A] = 1
    change_cnt = 0
    exist = False
    while not exist and q:
        change_cnt += 1
        new_q = deque()
        while q:
            now = q.popleft()
            for position, original_digit in enumerate(now):
                for new_digit in '0123456789':
                    if new_digit == original_digit: continue
                    new_num = now[:position] + new_digit + now[position + 1:]
                    if new_num == B: 
                        exist = True
                        break
                    if not is_prime[int(new_num)] or checked[new_num] != 0 or int(new_num) < 1000: continue
                    new_q.append(new_num)
                    checked[new_num] = 1
        q = new_q
    print(change_cnt if exist else "Impossible")
