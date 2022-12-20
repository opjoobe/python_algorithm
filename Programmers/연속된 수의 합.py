# 프로그래머스 # 연속된 수의 합
def solution(num, total):
    n, rest = divmod(num, 2)
    mid = total // num
    if rest == 0:
        return [x for x in range(mid - n + 1, mid + n + 1)]
    else:
        return [x for x in range(mid - n, mid + n + 1)]