# 프로그래머스 # 가장 긴 팰린드롬

def solution(s):
    # if len(set(s)) == len(s): return 1 # 있어도 큰 차이 못내주는듯
    n = len(s)
    for i in range(n, 0, -1): 
        for j in range(n-i+1): # 만약 i(길이)가 1이면, j는 0~n-1범위여야 한다. 마지막 j가 s[n-1:n]이 되도록!
            if s[j:j+i] == s[j:j+i][::-1]:
                return i