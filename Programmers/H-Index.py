# 프로그래머스 # H-Index 

def solution(citations):
    start, end = 0, len(citations)
    while start <= end:
        mid = (start + end) // 2
        nowUseCnt = len([x for x in citations if x >= mid])
        if nowUseCnt >= mid:
            start += 1
        else:
            end -= 1
    return end