# 프로그래머스 # 등수 매기기

def solution(score):
    score_d = dict()
    before_score, before_rank, i = 101, 0, 0
    for student, avg_score in sorted(enumerate(map(lambda x: sum(x)/2, score), 1), key = lambda x: -x[1]):
        i += 1
        if before_score == avg_score:
            score_d[student] = before_rank
        else:
            score_d[student] = i
            before_rank = i
        before_score = avg_score
    return [score_d[num] for num in range(1, len(score) + 1)]