# 프로그래머스 # 인덱스 바꾸기

def solution(my_string, num1, num2):
    num1, num2 = min(num1, num2), max(num1, num2) # assign smaller one to num1
    return my_string[ : num1] + my_string[num2] + my_string[num1 + 1 : num2] + my_string[num1] + my_string[num2 + 1 : ] # use indexing