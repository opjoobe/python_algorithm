# 프로그래머스 # 숫자 짝궁
from collections import Counter
def solution(X, Y):
    mutual = sorted(set(X).intersection(set(Y)), reverse = True)
    if not mutual: return "-1"
    if mutual[0] == '0': return '0'
    x_dict, y_dict = Counter(X), Counter(Y)
    return ''.join([str(i) * min(x_dict[i], y_dict[i]) for i in mutual])