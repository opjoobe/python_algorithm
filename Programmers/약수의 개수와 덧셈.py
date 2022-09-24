# 프로그래머스 # 약수의 개수와 덧셈

def solution(left, right):
    def divideCnt(N):
        total = 0
        for i in range(1, int(N ** (1/2))):
            if not N % i:
                total += 2
        if not N ** (1/2) % 1:
            total += 1
        return total
    answer = 0
    for num in range(left, right+1):
        nowCnt = divideCnt(num)
        print(num, nowCnt)
        if nowCnt % 2: 
            num = -num
        answer += num
    return answer