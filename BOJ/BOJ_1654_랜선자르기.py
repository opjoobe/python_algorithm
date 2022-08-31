# BOJ # 1654 # 랜선자르기
import sys
input = sys.stdin.readline

K, N = map(int, input().strip().split())

lines = [int(input()) for _ in range(K)]

start = 1
end = max(lines) # -1하면 틀림. max(lines)까지는 허용범위이기 때문.

while start <= end:
    mid = (start + end) // 2
    total = 0
    for line in lines:
        total += line // mid
    if total >= N:
        start = mid + 1
    else:
        end = mid -1
        
print(end)