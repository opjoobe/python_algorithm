# 프로그래머스 # 다음에 올 숫자
def solution(common):
    if common[2] - common[1] == common[1] - common[0]:
        return common[-1] + (common[1] - common[0])
    return common[-1] * (common[1] / common[0])