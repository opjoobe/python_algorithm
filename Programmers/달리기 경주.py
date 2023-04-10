# 프로그래머스 # 달리기 경주

def solution(players, callings):
    current_rank = dict(zip(players, range(len(players))))
    for calling in callings:
        now_rank = current_rank[calling]
        opponent = players[now_rank - 1]
        # swap
        players[now_rank - 1], players[now_rank] = players[now_rank], players[now_rank - 1]
        current_rank[opponent] += 1
        current_rank[calling] -= 1
    return players