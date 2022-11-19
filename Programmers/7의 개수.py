# 프로그래머스 # 7의 개수
def solution(array):
    return sum([str(num).count('7') for num in array])
