# 프로그래머스 # K번째 수

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]