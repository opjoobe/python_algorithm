# 프로그래머스 # N개의 최소공배수

def solution(arr):
    n = max(arr)
    now = n
    while True:
        flag = True
        for num in arr:
            if now % num:
                flag = False
                break
        if flag:
            return now
        now += n