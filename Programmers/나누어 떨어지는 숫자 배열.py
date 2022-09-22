# 프로그래머스 # 나누어 떨어지는 숫자 배열

# 풀이 1: 원래 풀이
def solution(arr, divisor):
    answer = [x for x in arr if not x % divisor]
    return sorted(answer) if answer else [-1]

# 풀이 2: return에 OR을 활용해 한줄로 나타내기
def solution(arr, divisor):
    return sorted([x for x in arr if not x % divisor]) or [-1]

'''
테스트 6에 대해 풀이 1 이 풀이 2에 비해 1ms 가량 빠름.
짧다고 마냥 좋은 것은 아닌듯.
'''