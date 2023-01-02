# 프로그래머스 # 이진수 더하기

def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2 : ]

'''
int(x, 2) : binary string x -> decimal int 
bin(y)    : decimal int y -> binary string ex) '0b1010'
'''