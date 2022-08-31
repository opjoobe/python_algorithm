# 블루레이
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
lessons = list(map(int, input().strip().split()))
MAX = 100000 * 10000

start = max(lessons) # 이게 중요함. 어떤 강의 딱 하나도 담지 못하는 블루레이는 의미가 없음.
end = MAX-1

while start <= end :
    mid = (start+ end) // 2 # 현재 블루레이 길이
    bluerayCnt = 1
    nowTotal = 0
    for lesson in lessons:
        nowTotal += lesson
        if nowTotal > mid:
            bluerayCnt += 1
            nowTotal = lesson
    if bluerayCnt <= M:
        end = mid - 1
    else:
        start = mid + 1
print(start)

    