# 프로그래머스 # 가운데 글자 가져오기

# 풀이 1 (if, else 포함한 기존 풀이)
def solution(s):
    return s[len(s)//2] if len(s) % 2 else s[len(s)//2-1] + s[len(s)//2]

# 풀이 2 (len(s)만 가지고 슬라이싱으로 풀어내는 방법)
def solution(s):
    return s[(len(s)-1)//2 : len(s)//2 + 1]