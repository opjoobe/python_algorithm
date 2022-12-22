# 프로그래머스 # 종이자르기
def solution(M, N):
    # if M > N : M, N = N, M
    # return (N - 1) + N * (M - 1)
    return M * N - 1 

'''
at first, i just found that in order to minimize the total cutting counts, 
split the page by min of (M rows, N cols): so it should be done by min(M, N) - 1 cutting counts,
and then cut the each section into 1 X 1 by max(M, N) * min(M, N) cutting counts.

so, I made M can always be minimum one, and the answer was (N-1) + N(M-1).
but it is exactly same with N - 1 + NM - N = NM - 1.  
in conclusion, we don't need to check which one is min or max. just simply calculate M * N - 1, and it will be the answer.
'''