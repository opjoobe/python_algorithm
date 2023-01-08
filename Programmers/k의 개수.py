#프로그래머스 #k의 개수

def solution(i, j, k):
    str_k = str(k)
    return sum(str(num).count(str_k) for num in range(i, j+1))
