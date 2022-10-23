# 프로그래머스 # 땅따먹기

def solution(land):
    before = [0, 0, 0, 0]
    for row in land:
        for col in range(4):
            row[col] += max([before[j] for j in range(4) if j != col])
        before = row
    return max(land[-1])