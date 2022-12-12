# 프로그래머스 # 문자열 정렬하기

''' 풀이 1 : my_string 길이가 매우 클 것을 생각하여 구성한 효율적인 풀이'''
from collections import defaultdict
def solution(my_string):
    alpha_dict = defaultdict(int)
    for letter in my_string:
        alpha_dict[letter.lower()] += 1
    answer = ''
    for num in range(97, 123):
        letter = chr(num)
        answer += letter * alpha_dict[letter]
    return answer

''' 풀이 2 : 파이썬용 쉬운 풀이'''
def solution(my_string):
    return ''.join(sorted(my_string.lower()))