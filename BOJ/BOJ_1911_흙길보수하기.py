# BOJ # 1911 # 흙길 보수하기
import sys
input = sys.stdin.readline
N, L = map(int, input().strip().split())
waters = [tuple(map(int, input().strip().split())) for _ in range(N)]
waters.sort(key = lambda x: x[0])

needs = 0
start, end = waters[0]
now, rest = divmod(end - start, L)
if rest:
    now += 1
    end += (L-rest) # 나머지(rest)에 L - rest를 더해줘야, L 길이의 널빤지가 마지막으로 설치된 위치를 알 수 있음.
needs += now
last = end
for start, end in waters[1:]:
    if end < last:  
        continue # 이 조건 추가로 12ms 단축 가능
    if start < last:
        start = last
    now, rest = divmod(end - start, L)
    if rest:
        now += 1
        end += (L-rest)
    needs += now
    last = end
print(needs)