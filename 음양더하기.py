# 프로그래머스 # 음양 더하기 # 3min sol

def solution(absolutes, signs):
    return sum([x if y else -x for x,y in zip(absolutes, signs)]) 
    
