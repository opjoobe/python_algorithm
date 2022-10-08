# 프로그래머스 # 진료순서 정하기

# 풀이 1
def solution(emergency):
    return [dict(zip(sorted(emergency, reverse = True), range(1, len(emergency)+1)))[x] for x in emergency]

# 풀이 2 : L.index(x) 활용하기
def solution(emergency):
    return [sorted(emergency, reverse = True).index(x)+1 for x in emergency]