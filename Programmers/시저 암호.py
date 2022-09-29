# 프로그래머스 # 시저 암호

def solution(s, n):
    return ''.join([chr((ord(c) - 65 + n) % 26 + 65) if c.isupper() else chr((ord(c) - 97 + n) % 26 + 97) if c.islower() else ' ' for c in s])

'''
파이썬에서는 list comprehension에서 if, elif, else 식으로 쓰고 싶다면,
[(IF조건 충족시 내줄 값) if (IF조건) else (ELSE IF 조건 충족시 내줄 값) if (ELSE IF 조건) else (ELSE 충족시 내줄 값)) for ITERATOR in MUTABLE DATA TYPE] 
이런 식으로 써야 한다.
예) ['A' if x > 0 else 'B' if x < 0 else 'C' for x in range(-1,5)]
'''