# 프로그래머스 # 합성수 찾기

def solution(n):
    is_composite = [0] * (n + 1)
    for num in range(2, int(n ** 0.5) + 1):
        if is_composite[num] == 0:
            for next_num in range(num * num, n + 1, num):
                is_composite[next_num] = 1
    return sum(is_composite)