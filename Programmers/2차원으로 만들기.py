#프로그래머스 #2차원으로 만들기

def solution(num_list, n):
    return [num_list[i * n : (i + 1) * n] for i in range(len(num_list) // n)] # use indexing.. ex) num_list[0:n], num_list[n:2n],...
