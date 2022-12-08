from heapq import heapify, heappush, heappop
def solution(n, k, enemy):
    stage_cnt = len(enemy)
    if k >= stage_cnt: return stage_cnt
    chance = enemy[:k]
    heapify(chance)
    for stage, stage_enemy in enumerate(enemy[k:], k + 1):
        if chance[0] < stage_enemy:
            heappush(chance, stage_enemy)
            stage_enemy = heappop(chance)
        n -= stage_enemy
        if n < 0: return stage - 1
    return stage_cnt