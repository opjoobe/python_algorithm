# BOJ # 1300 # K번째 수

import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

def get_less_cnt(target):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(target // i, N)
    return cnt

start  = 1
end = N ** 2

while start <= end:
    mid = (start + end) // 2
    print(mid)
    print(start, end)
    nowCnt = get_less_cnt(mid)
    if nowCnt >= k:
        end = mid - 1
    # 같을때 end를 줄이는 이유: nowCnt == k를 만족하는 가장 작은 경우를 찾아야 한다.
    # 가령 3*3 배열에서, 7보다 작은 숫자의 갯수는 6보다 작은 숫자의 갯수와 같음.  따라서 7이 아니라 6을 찾아주어야 함.
    else:
        start = mid + 1
        
print(start)




