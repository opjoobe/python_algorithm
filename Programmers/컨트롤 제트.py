# 프로그래머스 # 컨트롤 제트 
from functools import reduce
def solution(s):
    s_list = s.split()
    return reduce(lambda acc, cur: acc - int(s_list[cur - 1]) if s_list[cur] == 'Z' else acc + int(s_list[cur]), range(len(s_list)), 0)