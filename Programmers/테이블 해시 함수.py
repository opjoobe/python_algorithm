# 프로그래머스 # 테이블 해시 함수
def solution(data, col, row_begin, row_end):
    data.sort(key = lambda row: (row[col - 1], -row[0])) # sort by the given condition...
    answer = 0 # x ^ 0 = x , because XOR is like  1010 ^ 1100 = 0110 (different bit = 1, same bit = 0)
    for i in range(row_begin, row_end + 1):
        total = 0
        for field in data[i - 1]: # get S_i in the 'i'th row
            total += field % i 
        answer ^= total # repeat bitwise XOR ....
    return answer