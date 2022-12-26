# 프로그래머스 # 테이블 해시 함수
def solution(data, col, row_begin, row_end):
    data.sort(key = lambda row: (row[col - 1], -row[0])) # sort by the given condition...
    for i in range(row_begin, row_end + 1):
        total = 0
        # get S_i in the 'i'th row
        for field in data[i - 1]:
            total += field % i 
        if i == row_begin:
            answer = total # if i == row_begin, just initialize the answer with 'S_row_begin'
        else:
            answer ^= total # repeat bitwise XOR
    return answer